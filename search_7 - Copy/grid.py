import pymongo
import gridfs
clnt=pymongo.MongoClient('10.10.5.102',27017)
db=clnt.get_database("luozhitao")

fs=gridfs.GridFS(db)
file_id=fs.put("hello world")
f=fs.get(file_id).read()
print f
