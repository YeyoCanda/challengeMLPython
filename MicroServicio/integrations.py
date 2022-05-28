from urllib.request import urlopen
import urllib.parse, json, config

URL_ML_ITEMS = config.URL_ML_ITEMS
URL_ML_CATEGORY = config.URL_ML_CATEGORY
URL_ML_CURRENCY = config.URL_ML_CURRENCY
URL_ML_SELLER = config.URL_ML_SELLER

def getItemData(site, id):
    result = site + id                     
    param = {"ids":result}
    queryString = urllib.parse.urlencode(param) 
    urlItems = URL_ML_ITEMS + '?' + queryString
    response = urlopen(urlItems)
    data = json.loads(response.read())
    return data

def getCategoryName(itemCategoryId):
    categoryName = ''
    urlCategory = URL_ML_CATEGORY + itemCategoryId
    response = urlopen(urlCategory)
    data = json.loads(response.read())
    if "name" in data:
        categoryName = data["name"]
    return categoryName

def getCurrencyDescription(itemCurrencyId):
    currencyDescription = ''
    urlCurrency = URL_ML_CURRENCY + itemCurrencyId
    response = urlopen(urlCurrency)
    data = json.loads(response.read())
    if "description" in data:    
        currencyDescription = data["description"]
    return currencyDescription

def getSellerNickname(itemSellerId):
    sellerNickname = ''
    urlSeller = URL_ML_SELLER + str(itemSellerId)
    response = urlopen(urlSeller)
    data = json.loads(response.read())
    if "nickname" in data:
        sellerNickname = data["nickname"]
    return sellerNickname