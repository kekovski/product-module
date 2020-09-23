from database import Database
from pprint import pprint

Database.initialize()

product = {"name": "Mevlana cay",
           "supplier": "Mevlana",
           "origin": "Turkey"}

new_product = { "_id": {
                    "name": "Popkek",
               "supplier": "Eti",
               "origin": "Turkey"}
query = {"name": "Popkek"}

# Database.insert("products",product)
ret = Database.find_all("products")
print(ret)
for prod in ret:
    print(prod)

Database.insert("products",new_product)

ret = Database.find("products",query)
print("#####")
print(ret)