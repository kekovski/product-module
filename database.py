import pymongo
from pprint import pprint

class Database(object):
    URI = "localhost"
    PORT = 27017
    DATABASE = None

    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI,Database.PORT)
        Database.DATABASE = client['test_database']
        # Issue the serverStatus command and print the results
        # db = client.admin
        # serverStatusResult = db.command("serverStatus")
        # pprint(serverStatusResult)

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_all(collection):
        return Database.DATABASE[collection].find({})

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)