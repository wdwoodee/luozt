import pymongo
import csv
import os
import datetime
class device1():
    def conn(self):
            global connetion
            connetion=pymongo.MongoClient('10.10.5.199',27017)
    def find_db(self,dbname1,table1,table2,path):

        db1=connetion.get_database(dbname1)    ##NGTenantTemplate databse
        device_table=db1.get_collection(table1)

        devicetype_table=db1.get_collection(table2)
        _id='_id'
        typeName='typeName'
        mainType='mainType'
        vendor='vendor'
        action='action'
        enable='enable'
        parserOrder='parserOrder'

        name='name'
        path1=path+"\\chengpu.csv"
        csvfile=open(path1,'w',newline='')
        writer=csv.writer(csvfile)
        writer.writerow(['ID','Device Type','Category','Default Vendor','Support Operation','Status','Parse Order'])

        device_data1=device_table.find({},{_id:'True',typeName:'True',mainType:'True',vendor:'True',action:'True',enable:'True',parserOrder:'True'})
        for data in device_data1:
            ID=data[_id]
            DeviceType=data[typeName]
            devicetype_data=devicetype_table.find_one({_id:data[mainType]},{name:1})
            Category=devicetype_data[name]
            DefaultVendor=data[vendor]
            list_action=data[action]

            SupportOperation0=[]
            SupportOperation1={}
            SupportOperation2=[]

            for i in list_action:


                if (i['actionEnable']==True):

                    SupportOperation0.append(i['actionType'])
                    SupportOperation1[i['actionType']]='(1)'
                else:

                    SupportOperation0.append(i['actionType'])
                    SupportOperation1[i['actionType']]='(0)'

            SupportOperation0.sort()
            for k in SupportOperation0:
                SupportOperation2.append(str(k)+SupportOperation1[k])

            SupportOperation='|'.join(SupportOperation2)
            Status0=data[enable]
            if (Status0==True):
                Status='Enable'
            else:
                Status='Disable'
            ParseOrder=data[parserOrder]
            da=[ID,DeviceType,Category,DefaultVendor,SupportOperation,Status,ParseOrder]
            #print (da)
            writer.writerow(da)






if __name__=="__main__":
    path='D:\\search\\aa\\bb'
    print ("starting download data from mongodb,please wait......")
    datetime1=datetime.datetime.now()
    dbname1='NGTenantTemplate'
    table1='DeviceType'

    table2='DeviceMainType'
    de=device1()
    de.conn()
    de.find_db(dbname1,table1,table2,path)
    datetime2=datetime.datetime.now()
    print ("done! download data cost:"+str((datetime2-datetime1)))

