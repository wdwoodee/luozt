import datetime
import time
a="2016-02-19 06:21:31.615000"
b=a.replace(" ","-").replace(":","-").replace(".","-")
print b+'aaaa'
c=datetime.datetime.now()
time.sleep(5)
d=datetime.datetime.now()
print d-c
