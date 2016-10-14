import pika
import sys
import os
import pymongo
import datetime
import time
import logging
from  gridfs  import GridFS
from pika import exceptions

global connetion
connetion1=pymongo.MongoClient('10.10.5.133',27017)
path='D:\\search\\0603'
db=connetion1.get_database('0525_1')
table12=db.get_collection('DeviceDataSource')
table13=db.get_collection('Device')
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

#####################################
connection=pika.BlockingConnection(pika.ConnectionParameters(host='10.10.7.32'))
#connection.sleep(10)
channel=connection.channel()
channel.exchange_declare(exchange='topic_logs',type='topic')
channel.confirm_delivery()
result=channel.queue_declare(exclusive=True)
queue_name=result.method.queue
#severities=['routeTable*','config','showCommand','cdpTable','arpTable*','stpTable*','macTable*','commonTable*','nctTable*','bgpNbrTable*']
severities=['routeTableOrig','routeTable','config','showCommand','cdpTable','cdpTableOrig','arpTable','arpTableOrig','stpTable','stpTableOrig','macTable','macTableOrig','commonTable','commonTableOrig','nctTable','nctTableOrig','bgpNbrTable','bgpNbrTableOrig']

for severity in severities:
    #print(severity)
    channel.queue_bind(exchange='topic_logs',queue=queue_name,routing_key=severity)

def callback(ch,method,properities,body):
    a=eval(body)
    #print(a)
    key1=a.keys()
    if  fileId not in key1:
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
                                          with open(hostname2,'w') as f1:
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

                                          hostname_file=str(hostname1+"$$"+hostname_name+".txt").replace("X","XX").replace("*","XD").replace("/","XA").replace(":","XC").replace("<","XG").replace(">","XH").replace("|","XI").replace("\\","XB").replace("?","XE").replace('"','XF')
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
                                               with open(hostname4,'w') as f2:
                                                 f2.write(a[u'content'])
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
          if a[u'fileId']!=None:
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
                   print (fileid)
                   path2=path1+"\\"+str(fileid)+'.big'
                   f=fs.get(fileid).read()
                   with open(path2,'w') as f3:
                       f3.write(f)
    ch.basic_ack(delivery_tag = method.delivery_tag)
channel.basic_qos(prefetch_count=5)
channel.basic_consume(callback,queue=queue_name)

try:

    channel.start_consuming()

except pika.exceptions.ConnectionClosed:
    #connection.close()

    #time.sleep(5)
    logging.debug('reconnecting to queue')
    print ('reconnecting to queue')
    connection=pika.BlockingConnection(pika.ConnectionParameters(host='10.10.7.32'))
#connection.sleep(10)
    connection.sleep(60)
    channel=connection.channel()
    channel.confirm_delivery()
    #time.sleep(10)
    channel.exchange_declare(exchange='topic_logs',type='topic')
    result=channel.queue_declare(exclusive=True)
    queue_name=result.method.queue
#severities=['routeTable*','config','showCommand','cdpTable','arpTable*','stpTable*','macTable*','commonTable*','nctTable*','bgpNbrTable*']
    severities=['routeTableOrig','routeTable','config','showCommand','cdpTable','cdpTableOrig','arpTable','arpTableOrig','stpTable','stpTableOrig','macTable','macTableOrig','commonTable','commonTableOrig','nctTable','nctTableOrig','bgpNbrTable','bgpNbrTableOrig']

    for severity in severities:
        print(severity)
        channel.queue_bind(exchange='topic_logs',queue=queue_name,routing_key=severity)
    channel.basic_consume(callback,queue=queue_name)
    channel.start_consuming()
except exceptions as error:
    print (error)