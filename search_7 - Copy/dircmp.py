#-*-coding:utf-8-*-    
  
#===============================================================================  
# 目录对比工具(包含子目录 )，并列出
# 1、A比B多了哪些文件  
# 2、B比A多了哪些文件  
# 3、二者相同的文件:文件大小相同 VS 文件大小不同  (Size相同文件不打印:与Size不同文件显示未排序)
#===============================================================================  
  
import os, time,difflib


AFILES = []  #EE
BFILES = []  #SVN
COMMON = []  #EE & SVN
def getPrettyTime(state):
    return time.strftime('%y-%m-%d %H:%M:%S', time.localtime(state.st_mtime))

# def getpathsize(dir): #获取文件大小的函数,未用上,仅供学习.故注释掉
#     size=0
#     for root, dirs, files in os.walk(dir):
#     #root:目录:str 如: C:\CopySVN\SystemObject\TopoProcedure\Built-in\
#     #dirs:目录名称:列表: 如 ['Parsers']
#     #files:名称:列表: 如 ['011D0961FB42416AA49D5E82945DE7E9.og',...]
#     #file:目录:str, 如 011D0961FB42416AA49D5E82945DE7E9.og
#         for file in files:
#             path = os.path.join(root,file)
#             size = os.path.getsize(path)
#     return size

def dirCompare(apath,bpath):
    afiles = []
    bfiles = []
    for root, dirs , files in os.walk(apath):
        for f in files:
            afiles.append(root + "\\" + f)
    for root, dirs , files in os.walk(bpath):
        for f in files:
            bfiles.append(root + "\\" + f)
            #sizeB = os.path.getsize(root + "\\" + f) 此处定义的size无法在commonfiles进行比较. (A,B在各自的循环里面)

    # 去掉afiles中文件名的apath (拿A,B相同的路径\文件名,做成集合,去找交集)
    apathlen = len(apath)
    aafiles = []
    for f in afiles:
        aafiles.append(f[apathlen:])

    # 去掉bfiles中文件名的bpath
    bpathlen = len(bpath)
    bbfiles = []
    for f in bfiles:
        bbfiles.append(f[bpathlen:])
    afiles = aafiles
    bfiles = bbfiles
    setA = set(afiles)
    setB = set(bfiles)
    print('%$%'+str(len(setA)))
    print('%%'+str(len(setB)))
    commonfiles = setA & setB  # 处理共有文件
    #print ("===============File with different size in '", apath, "' and '", bpath, "'===============")
    #将结果输出到本地
    #with open(os.getcwd()+'diff.txt','w') as di:
        #di.write("===============File with different size in '", apath, "' and '", bpath, "'===============")
    for f in sorted(commonfiles):
        sA=os.path.getsize(apath + "\\" + f)
        sB=os.path.getsize(bpath + "\\" + f)
        if sA==sB:  #共有文件的大小比较
            #pass #print (f + "\t\t" + getPrettyTime(os.stat(apath + "\\" + f)) + "\t\t" + getPrettyTime(os.stat(bpath + "\\" + f)))
            #以下代码是处理大小一致，但是内容可能不一致的情况
            print("in sa=sb")
            print(os.getcwd())
            saf=[]
            sbf=[]
            sAfile=open(apath + "\\" + f)
            iter_f=iter(sAfile)
            for line in iter_f:
                saf.append(line)
            sAfile.close()
            sBfile=open(bpath + "\\" + f)
            iter_fb=iter(sBfile)
            for line in iter_fb:
                sbf.append(line)
            sBfile.close()
            saf1=sorted(saf)
            sbf1=sorted(sbf)
            if(len(saf1)!=len(sbf1)):
                with open(os.getcwd()+'\\comment_diff.txt','a') as fp:
                    print(os.getcwd())
                    fp.write(sAfile+" lines not equal "+sBfile+'\n')
            else:
                for i in range(len(saf1)):
                    if(saf1[i]!=sbf1[i]):
                        with open(os.getcwd()+'\\comment_diff.txt','a') as fp:
                            fp.write(sAfile+" comment not equal "+sBfile+'\n')


        else:
            with open (os.getcwd()+'\\diff.txt','w') as di:
                di.write("File Name=%s    EEresource file size:%d   !=  SVN file size:%d" %(f,sA,sB)+'\n')

            #print ("File Name=%s    EEresource file size:%d   !=  SVN file size:%d" %(f,sA,sB))

    # 处理仅出现在一个目录中的文件
    onlyFiles = setA ^ setB
    aonlyFiles = []
    bonlyFiles = []
    for of in onlyFiles:
        if of in afiles:
            aonlyFiles.append(of)
        elif of in bfiles:
            bonlyFiles.append(of)
    #print ("###################### EE resource ONLY ###########################")
    #print ("#only files in ", apath)
    for of in sorted(aonlyFiles):
        with open (os.getcwd()+'\\EEonly.txt','a') as ee:
            ee.write(of+'\n')

        #print (of)
    #print ("*"*20+"SVN ONLY+"+"*"*20)
    #print ("#only files in ", bpath)
    for of in sorted(bonlyFiles):
        with open (os.getcwd()+'\\svnonly.txt','a') as svn:
            svn.write(of+'\n')
        #print (of)
if __name__ == '__main__':
    FolderEE = 'D:\\search\\bb\\ObjectGroup - Copy\\ObjectGroup\\Built-in'
    FolderSVN = 'D:\\search\\bb\\ObjectGroup\\ObjectGroup\\Built-in'
    dirCompare(FolderEE, FolderSVN)
    print("done!")