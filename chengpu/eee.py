import random
aa=random.randint(0, 10000)
aa1="C:\\tt\\"+str(aa)+".txt"
with open(aa1,'a+') as ff:
    ff.write("sss")
    print (aa1)