# -*- coding: utf-8 -*-
import sys
#reload(sys)
sys.setdefaultencoding("utf-8")

import pymongo



import random, time, Queue
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager


global connetion
connetion=pymongo.MongoClient('192.168.30.79',27017)
#connection=pymongo.MongoClient('mongodb://10.10.5.216:27017')
dbs=connetion.database_names()
for i in dbs:
    print("mongdb connect successful")
    print (i+"\n")
db=connetion.get_database('5wdomian_0519')
table11=db.get_collection('DeviceData')
table12=db.get_collection('DeviceDataSource')
table13=db.get_collection('Device')
# ####################################################################
# 发送任务的队列:
task_queue = Queue.Queue(maxsize=100)
# 接收结果的队列:
result_queue = Queue.Queue()

# 从BaseManager继承的QueueManager:
class QueueManager(BaseManager):
    pass

def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def test():
    # 把两个Queue都注册到网络上, callable参数关联了Queue对象:
    # QueueManager.register('get_task_queue', callable=lambda: task_queue)
    # QueueManager.register('get_result_queue', callable=lambda: result_queue)
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000, 设置验证码'abc':
    manager = QueueManager(address=('192.168.30.72', 5001), authkey=b'abc')
    # 启动Queue:
    manager.start()
    # 获得通过网络访问的Queue对象:
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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
    dis_benchID='0d537ee8-ecec-4f45-9d52-e5660300d92d'
    k=0 
    type1=table11.find({sourceId:dis_benchID},{type:1,sourceId:1,devId:1,content:1,fileId:1,subName:1,name:1},no_cursor_timeout=True)
    type2=[]
    #%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    # 放几个任务进去:
    try:
      for i in type1:
         
        type2.append(i)
        if len(type2)==5:
          print (len(type2))          
          task.put(type2)
          type2=[]
          #print (i)
          k+=5
          print (k)
          print ('queue size is'+str(task.qsize()))
      if len(type2)!=0:
          task.put(type2)  
    except Exception as e:
          print (e)   
    # 从result队列读取结果:
    type1.close()
    print('Try get results...')
    #for i in range(100):
    r=result.get()
    #print (r)
     #   print('Result: %s' % r)
    # 关闭:
    while r=='done':
        manager.shutdown()
        print('master exit.')

if __name__ == '__main__':
    freeze_support()
    test()
