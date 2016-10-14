import os
import pymongo
import datetime
from  gridfs  import GridFS
global connetion
connetion=pymongo.MongoClient('10.10.5.102',27017)
db=connetion.get_database("luozhitao")
table1=db.get_collection("DeviceData")
#aa='config'
bb=table1.find({},{'type':'True'})
#for i in bb:
#    print str(i['type'])

cc=table1.find({'type':'config'})
print cc['type']