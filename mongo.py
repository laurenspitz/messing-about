#mongoDB test 

from pymongo import MongoClient
uri = "mongodb+srv://spitzlauried_db_user:AsJw5MTdfs9izy4x@demo.p3emiwy.mongodb.net/"
client = MongoClient(uri)
db = client["demo"] #db/demo is a database, which holds collections 
c = db["collectionTest"]

print("Testing!")
try:
    client.admin.command("ping")
    print("Connected successfully")

    #TESTING
    c.insert_one({"name" : "Python"})
    print("Current Collection:\n")
    all = c.find()
    for document in all : print(document)
    result = c.delete_many({})
    print("Deleted {result.length} documents.") #what should this be

    print("Current Collection:\n")
    all = c.find()
    for document in all : print("document")

    client.close()
except Exception as e:
    raise Exception(
        "The following error occurred: ", e)

