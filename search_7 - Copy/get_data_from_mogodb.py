import os
import re
import pymongo

#Rplace special character
#fortext=fortext.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("X","XX")
AllDevice_in_DB= 'Device'
AllGDF_in_DB = 'DeviceData'
Hostname = 'name'
Device_id = '_id'
DevId = 'devId'
SourceId = 'sourceId'
DataSourceId = '87db4f7d-7b16-fd52-6718-2201fecb0694'
content = 'content'
Type = 'type'
Subname = 'subName'
Vrf_key = 'vrf'
pcdir_config = r"D:\tmp\ConfigFile"
pcdir_routetable = r"D:\tmp\RoutingTable"
pcdir_ncttable = r"D:\tmp\CommonTable"
pcdir_showcommand = r"D:\tmp\ShowCommand"
 
def connMongo() :
    client = pymongo.MongoClient('10.10.5.102',27017)
    db = client.get_database('luozhitao')
    collection_device = db.get_collection(AllDevice_in_DB)
    AllDeviceData = db.get_collection(AllGDF_in_DB)
    device_looped = collection_device.find()

    for cur in device_looped :
        cur_config = AllDeviceData.find({SourceId:DataSourceId,DevId:str(cur[Device_id]),Type:'config'})
        #print str(cur[Device_id])
        for cur2 in cur_config :
            #Transfer "X" to "XX" at first
            host_name1 = str(cur[Hostname]).replace("X","XX")
            #Then Transfer other special characters
            host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
            #print host_name
            path_config=os.path.join(pcdir_config,host_name+".config")
            #print path_config
            ff=open(path_config,"w")
            ff.write(str(cur2[content]))
            ff.close()

        cur_routeTableOrig = AllDeviceData.find({SourceId:DataSourceId,DevId:str(cur[Device_id]),Type:'routeTableOrig'})
        for cur2 in cur_routeTableOrig :
            #vrf route table: cur2['subName'] = [u'subName': {u'vrf': u'Vrf-Testing'}]
            if (Subname in cur2.keys()) and (Vrf_key in cur2[Subname].keys()):
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #Join the vrf route file name: hostname+$+vrf name
                path_routetable_vrf=os.path.join(pcdir_routetable,host_name+"$"+str(cur2[Subname][Vrf_key])+".txt")
                #print path_routetable
                ff=open(path_routetable_vrf,"w")
                ff.write(str(cur2[content]))
                ff.close()
            else:
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #print host_name
                path_routetable=os.path.join(pcdir_routetable,host_name+".txt")
                #print path_routetable
                ff=open(path_routetable,"w")
                ff.write(str(cur2[content]))
                ff.close()  

        cur_routeTable = AllDeviceData.find({SourceId:DataSourceId,DevId:str(cur[Device_id]),Type:'routeTable'})
        for cur2 in cur_routeTable :
            #vrf route table: cur2['subName'] = [u'subName': {u'vrf': u'Vrf-Testing'}]
            if (Subname in cur2.keys()) and (Vrf_key in cur2[Subname].keys()):
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #Join the vrf route file name: hostname+$+vrf name
                path_routetable_vrf=os.path.join(pcdir_routetable,host_name+"$"+str(cur2[Subname][Vrf_key])+".ort")
                #print path_routetable
                ff=open(path_routetable_vrf,"w")
                ff.write(str(cur2[content]))
                ff.close()
            else:
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #print host_name
                path_routetable=os.path.join(pcdir_routetable,host_name+".ort")
                #print path_routetable
                ff=open(path_routetable,"w")
                ff.write(str(cur2[content]))
                ff.close()

        cur_nctTableOrig = AllDeviceData.find({SourceId:DataSourceId,DevId:str(cur[Device_id]),Type:'nctTable'})
        for cur2 in cur_nctTableOrig :
            #vrf route table: cur2['subName'] = [u'subName': {u'vrf': u'Vrf-Testing'}]
            if (Subname in cur2.keys()) and (Vrf_key in cur2[Subname].keys()):
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #Join the vrf route file name: hostname+$+vrf name
                path_ncttable_vrf=os.path.join(pcdir_ncttable,host_name+"$"+str(cur2["name"])+"$"+str(cur2[Subname][Vrf_key])+".txt")
                #print path_routetable
                ff=open(path_ncttable_vrf,"w")
                ff.write(str(cur2[content]))
                ff.close()
            else:
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #print host_name
                path_ncttable=os.path.join(pcdir_ncttable,host_name+"$"+str(cur2["name"])+".txt")
                ff=open(path_ncttable,"w")
                ff.write(str(cur2[content]))
                ff.close()   

        cur_nctTable = AllDeviceData.find({SourceId:DataSourceId,DevId:str(cur[Device_id]),Type:'nctTable'})
        for cur2 in cur_nctTable :
            #vrf route table: cur2['subName'] = [u'subName': {u'vrf': u'Vrf-Testing'}]
            if (Subname in cur2.keys()) and (Vrf_key in cur2[Subname].keys()):
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #Join the vrf route file name: hostname+$+vrf name
                path_ncttable_vrf=os.path.join(pcdir_ncttable,host_name+"$"+str(cur2["name"])+str(cur2[Subname][Vrf_key])+".csv")
                #print path_routetable
                ff=open(path_ncttable_vrf,"w")
                ff.write(str(cur2[content]))
                ff.close()
            else:
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #print host_name
                path_ncttable=os.path.join(pcdir_ncttable,host_name+"$"+str(cur2["name"])+".csv")
                #print path_routetable
                ff=open(path_ncttable,"w")
                ff.write(str(cur2[content]))
                ff.close()   

        cur_ShowCommand = AllDeviceData.find({SourceId:DataSourceId,DevId:str(cur[Device_id]),Type:'showCommand'})
        for cur2 in cur_ShowCommand :
            #print cur2
            #vrf route table: cur2['subName'] = [u'subName': {u'vrf': u'Vrf-Testing'}]
            if (Subname in cur2.keys()) and (Vrf_key in cur2[Subname].keys()):
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                #??show lldp neighbor Fa1/0/11 detail
                command_name = str(cur2["name"]).replace("/","XA").replace("|","XI")
                path_showcommand_vrf=os.path.join(pcdir_showcommand,host_name+"$"+command_name+str(cur2[Subname][Vrf_key])+".txt")
                #print path_routetable
                ff=open(pcdir_showcommand_vrf,"w")
                ff.write(str(cur2[content]))
                ff.close()
            else:
                #Transfer "X" to "XX" at first
                host_name1 = str(cur[Hostname]).replace("X","XX")
                #Then Transfer other special characters
                host_name = host_name1.replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB")
                ##??show lldp neighbor Fa1/0/11 detail
                command_name = str(cur2["name"]).replace("/","XA").replace("|","XI")
                path_showcommand=os.path.join(pcdir_showcommand,host_name+"$"+command_name+".txt")
                #print path_routetable
                ff=open(path_showcommand,"w")
                ff.write(str(cur2[content]))
                ff.close()

        #BGP Advertise-Route: type:"bgpNbrTable"; File name after parse: "host_name$neighbor_ip$default-live[$vrf_name].obgprt"

if __name__ == '__main__' :
       connMongo()

