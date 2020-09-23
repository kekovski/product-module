import pymongo
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint

class MongoDBConnect:

    @staticmethod
    def funcname(parameter_list):
        pass

    def funcname(self, parameter_list):
        pass
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient('localhost', 27017)
db = client.admin
# Issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)

db = client.test_database
# collection = db.test_collectio

collectionNames = "Collections in MongoDB: %s" % (db.list_collection_names())
print(collectionNames)
# product = {"name": "Mevlana cay",
#            "supplier": "Mevlana",
#            "origin": "Turkey"}

# collectionNames = "Collections in MongoDB: %s" % (db.list_collection_names())
# products = db.products
# product_id = products.insert_one(product).inserted_id

# msg = "Product ID of the newly created product is %s" % (product_id)
# print(msg)
# print(products.count()) 

# for product in products.find():
#     pprint(product)

# products.