import pymongo
import csv
import os
import datetime
class device1():
    def conn(self):
            global connetion
            connetion=pymongo.MongoClient('10.10.5.211',27017)
    def find_db(self,dbname1,table1,dbname2,table2,path):

        db1=connetion.get_database(dbname1)    ##domain databse
        device_table=db1.get_collection(table1)
        db2=connetion.get_database(dbname2)   ##tenant database
        devicetype_table=db2.get_collection(table2)
        name='name'
        mip='mip'
        mintf='mintf'
        subtype='subType'
        modules='modules'

        _id='_id'
        typeName='typeName'
        path1=path+"\\czhang.csv"
        csvfile=open(path1,'w')
        writer=csv.writer(csvfile)
        row_tiltle=[name,mip,mintf,typeName]
        row_tiltle1=[]


        device_data1=device_table.find({},{name:'True',mip:'True',mintf:'True',subtype:'True',modules:'True'})

        for data in device_data1:
            if ('modules' in data.keys()):
               if data[modules]!=None:
                   for i in data[modules]:
                       keys_m=i.keys()
                       for j in keys_m:
                           if j not in row_tiltle:
                               row_tiltle.append(j)
                               row_tiltle1.append(j)


        writer.writerow(row_tiltle)
        for data in device_data1:
            #print data[subtype]
            devicetype_data=devicetype_table.find_one({_id:data[subtype]})
            #print(data )




            typename1=devicetype_data[typeName]

            if mintf not in data:
                mintf_replace=' '
                data=[data[name],data[mip],mintf_replace,typename1]
            else:
                data=[data[name],data[mip],data[mintf],typename1]

            if ('modules' in data.keys()):
               if data[modules]!=None:
                   len_modules=len(data[modules])
                   for i in modules:
                       for j in row_tiltle1:
                           key1=i.keys()
                           if j not in key1:
                               data.append('')
                           else:
                               data.append(i[j])
                       writer.writerow(data)










    def calculate1(self,path):
       dirs=os.listdir(path)
       if (len(dirs)==0):
           print  ("there are no dir,please check it")

       for p in dirs:
            size = 0
            for root , dirs, files in os.walk(path+"\\"+p, True):
                   size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
            if (size>=1048576)and (size<1024*1048576):
                print( "discover --"+p+" size is "+str(size/float(1048576))+"M")
            elif (size>=1024*1048576) :
                print( "discover --"+p+" size is "+str(size/float(1048576*1024))+"G")
            else:
                print( "discover --"+p+" size is "+str(size)+"bytes")


    def check_fille(self,path):
        path5=path+"\\errdata\\errdata.txt"
        if os.path.exists(path5):
            print ("but there are some errdata ,plese see the file at "+path5)
        else:
            print ("there are no error data found!")


if __name__=="__main__":
    path='D:\\search\\aa\\bb'
    print ("starting download data from mongodb,please wait......")
    datetime1=datetime.datetime.now()
    dbname1='router'
    table1='Device'
    dbname2='czhang'
    table2='DeviceType'
    de=device1()
    de.conn()
    de.find_db(dbname1,table1,dbname2,table2,path)
    datetime2=datetime.datetime.now()
    print ("done! download data cost:"+str((datetime2-datetime1)))
    de.check_fille(path)
    print ("starting calculate files size,please wait.....")
    de.calculate1(path)
