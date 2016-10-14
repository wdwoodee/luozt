import os
import gridfs
path=["D:\\EE\\0120\\work\\userData\\Baseline\\a8000000000005\\ConfigFile\\","D:\\EE\\0120\\work\\userData\\Baseline\\a8000000000545\\ConfigFile\\"]
path1="D:\\personal\\device.csv"
if os.path.exists(path1):
    os.remove(path1)
with open(path1,'w') as f:
    f.write("##Table1"+"\n")
    f.write("var1"+"\n")
    for i in path:
      dir1=os.listdir(i)
      for item in dir1:
         if os.path.isfile(i+item):
           name1=item.split(".")
           if (len(name1)>2):
                   name2=item[:-7] #这么做的原因是为了让文件名中含有点号的文件
                   f.write('"'+name2+'"'+"\n") #加引号是为了处理hostname中含有逗号的情况
           else:
               f.write('"'+name1[0]+'"'+"\n")
