import redis

pool=redis.ConnectionPool(host='10.10.4.214',port=6379,db=0)
r=redis.Redis(connection_pool=pool)
pipe=r.pipeline(transaction=True)
r.set('name','zhangsan')
r.set('name1','lisi')
pipe.execute()
print(r.get('name'))




