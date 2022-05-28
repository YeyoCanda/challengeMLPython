import pymongo, config

URI_MONGODB = config.URI_MONGO
def connection():
    client = pymongo.MongoClient(URI_MONGODB)
    mydb = client["collection"]
    mycol = mydb["collection"]
    return mycol
    
#insert
def insertItemChallenge(item):
    mycol = connection()
    mycol.insert_one(item)

#delete
def deleteAllItemsChallenge():
    mycol = connection()
    x = mycol.delete_many({})
    return str(x.deleted_count) + " documents deleted"
