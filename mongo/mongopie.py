from pymongo import MongoClient

# class TestMongo:
#     def __init__(self):
client=MongoClient(host='localhost',port=27017)
db=client['lee']
collection=db['jaja']


result=collection.insert({'_id':'1','name':'lee'})
print(result)
