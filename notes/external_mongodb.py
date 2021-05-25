import pymongo

# Connects to the external machine
client = pymongo.MongoClient("mongodb://'ip_address':27017/demo")
db = client.demo

print(db.hello.find_one())