import pymongo


myclient = pymongo.MongoClient("mongodb+srv://<username>:<password>@cluster0.rxlsj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# db = myclient.test

database = myclient['sample_mflix']
collection = database['comments']

print(collection.count_documents({}))

some_select = collection.find({}, { "_id": 0, "name": 1 })
some_select.limit(5)
# some_select.sort([("name", 1)])

# print(myclient.list_database_names())
for i in some_select:
    print(i)