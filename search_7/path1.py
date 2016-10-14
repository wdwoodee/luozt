import os
dir1='D:\\search\\aa'
print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%55"

dirs=os.listdir(dir1)
print dirs
size = 0L
for p in dirs:

            for root , dirs, files in os.walk(dir1+"\\"+p, True):
                   size += sum([os.path.getsize(os.path.join(root, name)) for name in files])
            print( "discover --"+p+"size is "+str(size/float(1048576))+"M")