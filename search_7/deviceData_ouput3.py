import os
import pymongo
import datetime
from  gridfs  import GridFS
class DeviceData_out():

    def conn(self):
            global connetion
            connetion=pymongo.MongoClient('10.10.5.102',27017)
            #connection=pymongo.MongoClient('mongodb://10.10.5.216:27017')
            dbs=connetion.database_names()
            #for i in dbs:
             #   print("mongdb connect successful")
                #print (i+"\n")

    def find_db(self,dbname,table1,table2,table3,path):
            db=connetion.get_database(dbname)
            table11=db.get_collection(table1)
            table12=db.get_collection(table2)
            table13=db.get_collection(table3)

            type1=table11.find({},{'type':'True','sourceId':'True','devId':'True','content':'True','fileId':'True'})
            aa=[]
            bb=[]
            cc=[]
            aa=list(type1[:])
            for a in aa:
                key1=a.keys()
                if "u'fileId'" not in key1:
                 if len(a)!=5:
                   if not os.path.exists(path+"\\errdata"):
                       os.mkdir(path+"\\errdata")
                   else:
                       with open(path+"\\errdata\\errdata.txt",'a') as fe:
                           fe.write(str(a)+"\n")
                 else:
                   table22=table12.find({},{'startTime':'True'})
                   bb=list(table22[:])
                   table33=table13.find({},{'name':'True'})
                   cc=list(table33[:])
                   for b in bb:
                       if(a[u'sourceId']==b[u'_id']):
                           b1=str(b[u'startTime']).replace(" ","-").replace(":","-").replace(".","-")
                           path1=path+"\\"+b1
                           if not os.path.exists(path1):
                               os.mkdir(path1)
                           ty=a[u'type']
                           l1=len(ty)
                           if (ty[(l1-4):]=='Orig'):
                               path2=path1+"\\"+ty[0:(l1-4)]
                               if not os.path.exists(path2):
                                   os.mkdir(path2)
                               for c in cc:
                                   if (a[u'devId']==c[u'_id']):
                                       hostname1=str(c[u'name']+".txt").replace("/","-").replace("/","-").replace("\\","-").replace("|","-").replace(":","-").replace("*","-")
                                       hostname2=path2+"\\"+hostname1
                                       with open(hostname2,'w') as f1:
                                           f1.write(a[u'content'])



                           else:
                               path2=path1+"\\"+ty
                               if not os.path.exists(path2):
                                   os.mkdir(path2)
                               for c in cc:
                                   if (a[u'devId']==c[u'_id']):
                                       hostname3=str(c[u'name']+"$$default-live.oat").replace("/","-").replace("\\","-").replace("|","-").replace(":","-").replace("*","-")
                                       hostname4=path2+"\\"+hostname3
                                       with open(hostname4,'w') as f2:
                                           f2.write(a[u'content'])
                else:
                    fs=GridFS(db)
                    table22=table12.find({},{'startTime':'True'})
                    bb=list(table22[:])
                    table33=table13.find({},{'name':'True'})
                    cc=list(table33[:])
                    for b in bb:
                        if(a[u'sourceId']==b[u'_id']):
                           b1=str(b[u'startTime']).replace(" ","-").replace(":","-").replace(".","-")
                           path1=path+"\\"+b1
                           if not os.path.exists(path1):
                               os.mkdir(path1)
                           fileid=a[u'fileId']
                           path2=path1+"\\"+fileid+'.big'
                           f=fs.get(fileid).read()
                           with open(path2,'w') as f3:
                               f3.write(f)


    def calculate1(self,path):
       dirs=os.listdir(path)
       if (len(dirs)==0):
           print "there are no dir,please check it"

       for p in dirs:
            size = 0L
            for root , dirs, files in os.walk(path+"\\"+p, True):
                   size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
            if (size>=1048576):
                print( "discover --"+p+" size is "+str(size/float(1048576))+"M")
            elif (size>=1024*1048576):
                print( "discover --"+p+" size is "+str(size/float(1048576*1024))+"G")
            else:
                print( "discover --"+p+" size is "+str(size)+"bytes")


    def check_fille(self,path):
        path5=path+"\\errdata\\errdata.txt"
        if os.path.exists(path5):
            print ("but there are some errdata ,plese see the file at "+path5)
        else:
            print "there are no error data found!"


if __name__=="__main__":
    path='D:\\search\\aa'
    print ("starting download data from mongodb,please wait......")
    datetime1=datetime.datetime.now()

    de=DeviceData_out()
    de.conn()
    de.find_db("luozhitao","DeviceData","DeviceDataSource","Device",path)
    datetime2=datetime.datetime.now()
    print ("done! download data cost:"+str((datetime2-datetime1)))
    de.check_fille(path)
    print ("starting calculate files size,please wait.....")
    de.calculate1(path)
