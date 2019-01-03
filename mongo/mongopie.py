from pymongo import MongoClient

# class TestMongo:
#     def __init__(self):
client=MongoClient(host='localhost',port=27017)
db=client['lee']
collection=db['jaja']

# #insert one
result=collection.insert({'_id':'2','name':'le'})
print(result)

# #insert many
item_list=[{'name':'test{}'.format(i)} for i in range(10)]
t=collection.insert_many(item_list)
for i in t.inserted_ids:
    print(i)

#find_one
t=collection.find_one({'name':'test5'})
print(t)

#find_many
t=collection.find({'name':'test5'})
for i in t:
    print(i)
for i in t:
    print(i)

#update_one
collection.update_one({'name':'test6'},{"$set":{'name':'new_test6'}})

#update_many
collection.update_many({'name':'test1'},{'$set':{'name':'new_test1')})

#delete one
collection.delete_one({'name':'new_test9'})

#delete many
collection.delete_many({'name':'new_test9'})
