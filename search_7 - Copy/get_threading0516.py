import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import os
import pymongo
import datetime
from  gridfs  import GridFS

import threading
class DeviceData_out():

    def conn(self):
            global connetion
            connetion=pymongo.MongoClient('10.10.5.246',27018)
            #connection=pymongo.MongoClient('mongodb://10.10.5.216:27017')
            dbs=connetion.database_names()
            for i in dbs:
                print("mongdb connect successful")
                print (i+"\n")

    def find_db(self,dbname,table1,table2,table3,path,flag1,discover_name):
            db=connetion.get_database(dbname)
            table11=db.get_collection(table1)
            table12=db.get_collection(table2)
            table13=db.get_collection(table3)
            type='type'
            sourceId='sourceId'
            devId='devId'
            content='content'
            fileId='fileId'
            subName='subName'
            name='name'






            aa=[]
            bb=[]
            cc=[]
            #aa=list(type1[:])
            config='config'
            cdpTable='cdpTable'
            routeTable='routeTable'
            showCommand='showCommand'
            arpTable='arpTable'
            stpTable='stpTable'
            macTable='macTable'
            commonTable='commonTable'
            nctTable='nctTable'
            bgpNbrTable='bgpNbrTable'
            dis_benchID='ec5aad5e-ce6d-4dfc-a8ba-5a8e66ba2593'
            device_type=['routeTableOrig','routeTable','config','showCommand','cdpTable','cdpTableOrig','arpTable','arpTableOrig','stpTable','stpTableOrig','macTable','macTableOrig','commonTable','commonTableOrig','nctTable','nctTableOrig','bgpNbrTable','bgpNbrTableOrig']

            def get_thread(self,k):

                    type1=table11.find({type:k,sourceId:dis_benchID},{type:1,sourceId:1,devId:1,content:1,fileId:1,subName:1,name:1},no_cursor_timeout=True)
                    #type1=table11.find({sourceId:dis_benchID},{type:1,sourceId:1,devId:1,content:1,fileId:1,subName:1,name:1},no_cursor_timeout=True)
                    for a in type1:

                        key1=a.keys()
                        if fileId not in key1:
                         #if len(a)!=5:

                         if  sourceId not in key1:
                           if not os.path.exists(path+"\\errdata"):
                               os.mkdir(path+"\\errdata")
                           else:
                               with open(path+"\\errdata\\errdata.txt",'a') as fe:
                                   fe.write(str(a)+"\n")
                         else:


                           #bb=list(table22[:])

                           #cc=list(table33[:])
                           table22=table12.find({},{'startTime':'True','srcType':'True'},no_cursor_timeout=True)
                           table33=table13.find({},{'name':'True','mip':'True'},no_cursor_timeout=True)
                           for b in table22:
                               if(a[u'sourceId']==b[u'_id']):
                                   b1=(str(b[u'startTime'])+str(b[u'srcType'])).replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                   path1=path+"\\"+b1
                                   if not os.path.exists(path1):
                                       os.mkdir(path1)
                                   ty=str(a[u'type'])

                                   l1=len(str(ty))
                                   if (ty[(l1-4):]=='Orig'):
                                       if(ty[0:(l1-4)]==arpTable):
                                           typename='ArpTable'
                                       elif(ty[0:(l1-4)]==cdpTable):
                                           typename='CdpTable'
                                       elif(ty[0:(l1-4)]==bgpNbrTable):
                                           typename='BGPAdRoutingTable'
                                       elif(ty[0:(l1-4)]==routeTable):
                                           typename='RoutingTable'
                                       elif(ty[0:(l1-4)]==config):
                                           typename='ConfigFile'
                                       elif(ty[0:(l1-4)]==showCommand):
                                           typename='ShowCommand'
                                       elif(ty[0:(l1-4)]==stpTable):
                                           typename='StpTable'
                                       elif(ty[0:(l1-4)]==macTable):
                                           typename='MacTable'
                                       elif(ty[0:(l1-4)]==nctTable):
                                           typename='CommonTable'
                                       else:typename='unkown'+ty
                                       path2=path1+"\\"+typename
                                       if not os.path.exists(path2):
                                           os.mkdir(path2)

                                       for c in table33:
                                           if (a[u'devId']==c[u'_id']):
                                             if(ty[0:(l1-4)]==arpTable):
                                               if  "subName" in key1:
                                                   hostname1=str(c[u'name']+"$management.txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                   hostname2=path2+"\\"+hostname1
                                                   with open(hostname2,'w') as f1:
                                                       f1.write(a[u'content'])
                                               else:
                                                   hostname1=str(c[u'name']+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                   hostname2=path2+"\\"+hostname1
                                                   with open(hostname2,'w') as f1:
                                                       f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==cdpTable):
                                                  hostname1=str(c[u'name']+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname1
                                                  with open(hostname2,'w') as f1:
                                                   f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==routeTable):
                                                  hostname1=str(c[u'name'])
                                                  if "subName" in key1:
                                                      hostname_file=str(hostname1+"$"+a[u'subName']['vrf']+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                      hostname2=path2+"\\"+hostname_file
                                                      with open(hostname2,'w') as f1:
                                                          f1.write(a[u'content'])
                                                  else:
                                                      hostname_file=str(hostname1+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                      hostname2=path2+"\\"+hostname_file
                                                      with open(hostname2,'w') as f1:
                                                          f1.write(a[u'content'])

                                             elif(ty[0:(l1-4)]==showCommand):
                                                  hostname1=str(c[u'name']+"$0$"+a[u'name']+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname1
                                                  with open(hostname2,'w') as f1:
                                                   f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==config):
                                                  hostname1=str(c[u'name']+".config").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname1
                                                  with open(hostname2,'wb') as f1:
                                                   f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==macTable):
                                                  hostname1=str(c[u'name']+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname1
                                                  with open(hostname2,'w') as f1:
                                                   f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==stpTable):
                                                  hostname1=str(c[u'name']+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname1
                                                  with open(hostname2,'w') as f1:
                                                   f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==bgpNbrTable):
                                                if "subName" in key1:
                                                  hostname1=str(c[u'name'])
                                                  hostname_ip=a[u'subName']['peIp']
                                                  key2=a[u'subName'].keys()
                                                  if "vrf" in a[u'subName'].keys():
                                                      hostname_vrf=a[u'subName']['vrf']
                                                      hostname_file=str(hostname1+"$"+hostname_ip+"$"+hostname_vrf+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                      hostname2=path2+"\\"+hostname_file
                                                      with open(hostname2,'w') as f1:
                                                         f1.write(a[u'content'])
                                                  else:
                                                      hostname_file=str(hostname1+"$"+hostname_ip+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                      hostname2=path2+"\\"+hostname_file
                                                      with open(hostname2,'w') as f1:
                                                         f1.write(a[u'content'])

                                                else:
                                                  hostname1=str(c[u'name'])
                                                  hostname_ip=c[u'mip']
                                                  hostname_file=str(hostname1+"$"+hostname_ip+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname_file
                                                  with open(hostname2,'w') as f1:
                                                   f1.write(a[u'content'])
                                             elif(ty[0:(l1-4)]==nctTable):

                                                  hostname1=str(c[u'name'])
                                                  hostname_name=a[u'name']

                                                  hostname_file=str(hostname1+"$$"+hostname+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                  hostname2=path2+"\\"+hostname_file
                                                  with open(hostname2,'w') as f1:
                                                   f1.write(a[u'content'])





                                   else:
                                       if(ty==arpTable):
                                           typename='ArpTable'
                                       elif(ty==cdpTable):
                                           typename='CdpTable'
                                       elif(ty==bgpNbrTable):
                                           typename='BGPAdRoutingTable'
                                       elif(ty==routeTable):
                                           typename='RoutingTable'
                                       elif(ty==config):
                                           typename='ConfigFile'
                                       elif(ty==showCommand):
                                           typename='ShowCommand'
                                       elif(ty==stpTable):
                                           typename='StpTable'
                                       elif(ty==macTable):
                                           typename='MacTable'
                                       elif(ty==nctTable):
                                           typename='CommonTable'
                                       else:typename='unkown'+ty
                                       path2=path1+"\\"+typename
                                       if not os.path.exists(path2):
                                           os.mkdir(path2)
                                       for c in table33:
                                           if (a[u'devId']==c[u'_id']):
                                               if(ty==arpTable):
                                                   hostname=str(c[u'name'])
                                                   if "subName" in key1:
                                                       hostname_vrf=a[u'subName']['vrf']
                                                       filename=str(hostname+"$"+hostname_vrf+"$"+"default-live.oat").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                                   else:
                                                       filename=str(hostname+"$$"+"default-live.oat").replace("*","XD").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==cdpTable):
                                                   hostname=str(c[u'name'])
                                                   if "subName" in key1:
                                                       hostname_vrf=a[u'subName']['vrf']
                                                       filename=str(hostname+"$"+hostname_vrf+"$"+"default-live.cdp").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                                   else:
                                                       filename=str(hostname+"$$"+"default-live.cdp").replace("*","XD").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==routeTable):
                                                   hostname=str(c[u'name'])
                                                   if "subName" in key1:
                                                       hostname_vrf=a[u'subName']['vrf']
                                                       filename=str(hostname+"$"+hostname_vrf+"$"+"default-live.ort").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                                   else:
                                                       filename=str(hostname+"$$"+"default-live.ort").replace("*","XD").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==showCommand):
                                                       hostname=str(c[u'name'])
                                                       hostname_vrf=str(a[u'name'])
                                                       filename=str(hostname+"$0$"+hostname_vrf+".txt").replace("*","XD").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==config):
                                                       hostname=str(c[u'name']).replace("*","XD").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')

                                                       filename=hostname+".config"
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'wb') as f2:
                                                         f2.write(a[u'content'].decode('utf8'))
                                               elif(ty==macTable):
                                                   hostname=str(c[u'name'])
                                                   if "subName" in key1:
                                                       hostname_vrf=a[u'subName']['vrf']
                                                       filename=str(hostname+"$"+hostname_vrf+"$"+"default-live.omt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                                   else:
                                                       filename=str(hostname+"$$"+"default-live.omt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==stpTable):
                                                   hostname=str(c[u'name'])
                                                   if "subName" in key1:
                                                       hostname_vrf=a[u'subName']['vrf']
                                                       filename=str(hostname+"$"+hostname_vrf+"$"+"default-live.stp").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                                   else:
                                                       filename=str(hostname+"$$"+"default-live.stp").replace("*","XD").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==bgpNbrTable):
                                                   hostname=str(c[u'name'])
                                                   if "subName" in key1:
                                                       hostname_ip=a[u'subName']['peIp']
                                                       if "vrf" in a[u'subName'].keys():
                                                           hostname_vrf=a[u'subName'][u'vrf']
                                                           filename=str(hostname+"$"+hostname_ip+"$"+"default-live"+"$"+hostname_vrf+".obgprt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                           hostname4=path2+"\\"+filename
                                                           with open(hostname4,'w') as f2:
                                                              f2.write(a[u'content'])
                                                       else:
                                                           filename=str(hostname+"$"+hostname_ip+"$"+"default-live.obgprt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                           hostname4=path2+"\\"+filename
                                                           with open(hostname4,'w') as f2:
                                                              f2.write(a[u'content'])

                                                   else:
                                                       hostname_ip=c[u'mip']

                                                       filename=str(hostname+"$"+hostname_ip+"$"+"default-live.obgprt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                                               elif(ty==nctTable):
                                                       hostname=str(c[u'name'])

                                                       hostname_name=a[u'name']

                                                       filename=str(hostname+"$$"+hostname_name+".csv").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                                       hostname4=path2+"\\"+filename
                                                       with open(hostname4,'w') as f2:
                                                         f2.write(a[u'content'])
                           table33.close()
                           table22.close()





                        else:
                            fs=GridFS(db)
                            table22=table12.find({},{'startTime':'True'})
                            bb=list(table22[:])
                            table33=table13.find({},{'name':'True'})
                            cc=list(table33[:])
                            for b in bb:
                                if(a[u'sourceId']==b[u'_id']):
                                   b1=str(b[u'startTime']).replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
                                   path1=path+"\\"+b1
                                   if not os.path.exists(path1):
                                       os.mkdir(path1)
                                   fileid=a[u'fileId']
                                   path2=path1+"\\"+fileid+'.big'
                                   f=fs.get(fileid).read()
                                   with open(path2,'w') as f3:
                                       f3.write(f)
                    type1.close()
            def main(self):
                    threadingpool=[]
                    for i in device_type:
                        th=threading.Thread(target=get_thread,args=(i))
                        threadingpool.append(th)
                    for th in threadingpool:
                        th.start()
                    for th in threadingpool:
                        threading.Thread.join(th)
            main()
    def calculate1(self,path):
       dirs=os.listdir(path)
       if (len(dirs)==0):
           print "there are no dir,please check it"

       for p in dirs:
            size = 0L
            for root , dirs, files in os.walk(path+"\\"+p, True):
                   size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
            if (size>=1048576)and (size<1024*1048576):
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

    def replace_str(self,str):
        str=str.replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
        return str


if __name__=="__main__":
    path='D:\\search\\0516'
    print ("starting download data from mongodb,please wait......")
    datetime1=datetime.datetime.now()
    flag1=0
    discover_name=''
    dbname='0511_1'
    DeviceData='DeviceData'
    DeviceDataSource='DeviceDataSource'
    Device='Device'

    de=DeviceData_out()
    de.conn()
    de.find_db(dbname,DeviceData,DeviceDataSource,'Device',path,flag1,discover_name)
    datetime2=datetime.datetime.now()
    print ("done! download data cost:"+str((datetime2-datetime1)))
    de.check_fille(path)
    print ("starting calculate files size,please wait.....")
    de.calculate1(path)
