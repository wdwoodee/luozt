import os
import gridfs
path="C:\\Users\\luozhitao\\Desktop\\server1to5.discoverylist.txt"
f=file(path);
k=1
name2=[]
b={}
for i in f:
    name1=i.split(";")
    for j in name1:
 #       print 'num is '+str(k)+'***'+str(j)
        k=k+1
        name2.append("'"+j+"'")
        with open ('C:\\Users\\luozhitao\\Desktop\\server1to5.discoverylist112.txt','a') as ff1:
            ff1.write('num is '+str(k)+'***'+str(j)+'\n')
        if name1.count(j)>1:
            print (j+'count is '+str(name1.count(j)))

    print len(name1)
    with open ('C:\\Users\\luozhitao\\Desktop\\server1to5.discoverylist11.txt','w') as ff:
        ff.write(','.join(name2))

