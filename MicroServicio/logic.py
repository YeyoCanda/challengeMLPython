from flask import make_response, jsonify, request
from concurrent.futures import ThreadPoolExecutor
import integrations, model, config
def createData():
    try:
        req = request.get_json()
        fileName = req["route"]+"."+req["format"]
        file = open(fileName, 'r', encoding=req["encoding"])
        next(file)
        with ThreadPoolExecutor (max_workers=config.NUM_OF_THREADS) as executor:
            for line in file:
                lineSplited = line.split(req["separator"])
                site = lineSplited[0]
                id = lineSplited[1].rstrip('\n')
                if site and id:
                    executor.submit(processData,site, id)
        file.close()
        return make_response(jsonify({"Success": "The process ended successfully"}), 200)
    except Exception as e:
        if not file.closed: 
            file.close()
        return make_response(jsonify({"error": "An exception occurred " + str(e)}), 400)

def processData(site, id):
    data = integrations.getItemData(site, id)
    if data:
        item = data[0]
        if(item["code"] == 200):
            body = item["body"]
            itemStartTime = body["start_time"] if "start_time" in body else ""
            itemPrice = body["price"] if "price" in body else ""
            categoryName = ''
            if "category_id" in body:
                categoryName = integrations.getCategoryName(body["category_id"])
            currencyDescription = ''
            if "currency_id" in body:
                currencyDescription = integrations.getCurrencyDescription(body["currency_id"])
            sellerNickname = ''
            if "seller_id" in body:
                sellerNickname = integrations.getSellerNickname(str(body["seller_id"]))
            formatDataItemToInsert(site,id,itemPrice,itemStartTime,categoryName,currencyDescription,sellerNickname)


def formatDataItemToInsert(site,id,itemPrice,itemStartTime,categoryName,currencyDescription,sellerNickname):
    item = {
        "site":site,
        "id":id,
        "itemPrice":itemPrice,
        "itemStartTime":itemStartTime,
        "categoryName":categoryName,
        "currencyDescription":currencyDescription,
        "sellerNickname":sellerNickname
    }
    model.insertItemChallenge(item)  

def deleteItems():
    try:
        return make_response(jsonify(model.deleteAllItemsChallenge()), 200)
    except Exception as e:
        return make_response(jsonify({"error": "An exception occurred " + str(e)}), 400)