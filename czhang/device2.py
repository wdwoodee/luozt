import pymongo
import csv
import os
import datetime
class device1():
    def conn(self):
            global connetion
            connetion=pymongo.MongoClient('10.10.5.224',27017)
    def find_db(self,dbname1,table1,path):

        db1=connetion.get_database(dbname1)    ##domain databse
        device_table=db1.get_collection(table1)
        name='name'
        modules='modules'

        _id='_id'
        path1=path+"\\modules.csv"
        csvfile=open(path1,'wb')
        writer=csv.writer(csvfile)
        row_tiltle=['device_name']
        row_tiltle1=[]


        device_data1=device_table.find({},{name:'True',modules:'True'})

        for data in device_data1:
            if ('modules' in data.keys()):
               if data[modules]!=None:
                   for i in data[modules]:
                       keys_m=i.keys()
                       for j in keys_m:
                           if j not in row_tiltle1:
                               row_tiltle.append(j)
                               row_tiltle1.append(j)


        writer.writerow(row_tiltle)
        device_data1=device_table.find({},{name:'True',modules:'True'})
        for data in device_data1:
            #print data[subtype]

            if ('modules' in data.keys()):
               if data[modules]!=None:


                   for i in data[modules]:
                       data1=[]
                       data1.append(data[name])
                       for j in row_tiltle1:
                           key1=i.keys()
                           #print key1

                           if j not in key1:
                               data1.append('')
                           else:
                               data1.append(i[j])

                       writer.writerow(data1)










if __name__=="__main__":
    path='D:\\search\\cc'
    print ("starting download data from mongodb,please wait......")
    datetime1=datetime.datetime.now()
    dbname1='czhang_1'
    table1='Device'
    de=device1()
    de.conn()
    de.find_db(dbname1,table1,path)
    datetime2=datetime.datetime.now()
