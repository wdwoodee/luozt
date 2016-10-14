import pymongo
import csv
import os
import datetime
class interface():
    def conn(self):
            global connetion
            connetion=pymongo.MongoClient('10.10.5.224',27017)
    def find_db(self,dbname1,table1,table2,path):

        db1=connetion.get_database(dbname1)                   ##domain databse
        interface_table=db1.get_collection(table1)               ##interface table
        devicename_table=db1.get_collection(table2)             ##device table
        name='name'                     ### def $ 
        mib_index='iMibIndex'
        bandwidth='bandwidth'
        speed='speed'
        duplex="duplex"
        status="interfaceStatus"
        mac="macAddr"
        slot="moduleSlot"
        module_type="moduleType"
        description="descr"
        devId='devId'
        _id='_id'
        deviceName='name'
        ips='ips'
        ipLoc='ipLoc'
        ips_null=''
        path1=path+"\\7.0 interface properties.csv"          
        csvfile=file(path1,'wb')
        writer=csv.writer(csvfile)
        writer.writerow(["device_name","if_name","mib_index","bandwidth","speed","duplex","live_status","mac_address","slot_no","module_type","description",ipLoc])
        #####def CSV colum name
        
        interface_data1=interface_table.find({},{name:'True',mib_index:'True',bandwidth:'True',speed:'True',duplex:'True',status:'True',mac:'True',slot:'True',module_type:'True',description:'True',devId:'True',ips:'True'})
        #####get data from db 
        
        for data in interface_data1:
            #print data[subtype]
            if mib_index not in data:             ##Not null
                mib_null='NUL'
            else:
                mib_null=data[mib_index]  
            if  bandwidth not in data:
                bd_null='NUL'
            else:
                bd_null=data[bandwidth]        
            if speed not in data:
                speed_null='NUL'
            else:
                speed_null=data[speed]      
            if duplex not in data:
                dup_null='NUL'
            else:
                dup_null=data[duplex]
            if status not in data:
                status_null='NUL'
            else:
                status_null=data[status]  
            if mac not in data:
                mac_null='NUL'
            else:
                mac_null=data[mac]   
            if slot not in data:
                slot_null='NUL'
            else:
                slot_null=data[slot] 
            if module_type not in data:
                module_null='NUL'
            else:
                module_null=data[module_type]   
            if description not in data:
                des_null='NUL'
            else:
                des_null=data[description]
            if ips not in data:
                ips_null='NUL'
            else:
                if data[ips]!=None:
                    ips_data=data[ips]
                    ips_data1=[]
                    for k in ips_data:
                        ips_data1.append(str(k[ipLoc]).split('/')[0])
                    ips_null='\n'.join(ips_data1)

            devicename_data=devicename_table.find_one({_id:data[devId]}) if data and devId in data else ''
            devicename1=devicename_data[deviceName] if devicename_data else 'NUL'
            data=[devicename1,data[name] if name in data else 'NUL',mib_null,bd_null,speed_null,dup_null,status_null,mac_null,slot_null,module_null,des_null,ips_null]
            writer.writerow(data)






if __name__=="__main__":
    path='D:\\search\\cc'
    print ("starting download data from mongodb,please wait......")
    datetime1=datetime.datetime.now()
    dbname1='czhang_bj'
    table1='Interface'
    table2='Device'
    de=interface()
    de.conn()
    de.find_db(dbname1,table1,table2,path)
    datetime2=datetime.datetime.now()
    print ("done! download data cost:"+str((datetime2-datetime1)))
  
