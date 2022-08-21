import pymongo


client = pymongo.MongoClient("mongodb+srv://Virendra_Singh:Virendra@cluster0.dkfrhpm.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name": "Virendra",
    "email" : "Virendra@gmail.com",
    "surname": "Bhandari"
}

db1 = client['mongotest']
coll = db1['test']

coll.insert_one(d)