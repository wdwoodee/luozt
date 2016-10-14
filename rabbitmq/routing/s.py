import pika
import sys
import pymongo
#mongodb 配置
global connetion
connetion1=pymongo.MongoClient('10.10.5.133',27017)
db=connetion1.get_database('0525_1')
table11=db.get_collection('DeviceData')
table12=db.get_collection('DeviceDataSource')
table13=db.get_collection('Device')


# rabbitmq 配置
connection=pika.BlockingConnection(pika.ConnectionParameters(host='10.10.7.32'))
channel=connection.channel()
channel.confirm_delivery()
channel.exchange_declare(exchange='topic_logs',type='topic')
#severities=[]
severities=['routeTableOrig','routeTable','config','showCommand','cdpTable','cdpTableOrig','arpTable','arpTableOrig','stpTable','stpTableOrig','macTable','macTableOrig','commonTable','commonTableOrig','nctTable','nctTableOrig','bgpNbrTable','bgpNbrTableOrig']

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
type='type'
sourceId='sourceId'
devId='devId'
content='content'
fileId='fileId'
subName='subName'
name='name'
dis_benchID='46da508d-b42e-1de3-7a40-1a95878bf014'
type1=table11.find({sourceId:dis_benchID},{type:1,sourceId:1,devId:1,content:1,fileId:1,subName:1,name:1},no_cursor_timeout=True)

try:
    for i in type1:
        #rk=bytes(i[type],encoding="utf8")
        print (i[type])
        channel.basic_publish(exchange='topic_logs',routing_key=i[type],body=str(i),properties=pika.BasicProperties(delivery_mode = 2,))

except Exception as e:
    print (e)
type1.close()
connection.close()