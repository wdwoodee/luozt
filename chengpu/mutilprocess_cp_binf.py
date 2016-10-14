__author__ = 'caohuan'
import telnetlib
import multiprocessing
import random
def telnet(ip,hostname):

    tn = telnetlib.Telnet(ip)
    print("begin telnet "+str(hostname)+"...")
    tn.read_until("Username:".encode('ascii'))

    tn.write("nb".encode('ascii')+b"\n")

    tn.read_until(b"Password:")
    tn.write("nb".encode('ascii') + b"\n")

    print(hostname.encode('ascii'))

    tn.read_until(hostname.encode('ascii')+ b">")


    tn.write("enable".encode('ascii') + b"\n")

    tn.read_until("Password:".encode('ascii'))
    tn.write("nb".encode('ascii') + b"\n")

    tn.read_until(hostname.encode('ascii')+b'#')

    tn.write("terminal length 0".encode('ascii') + b"\n")
    tn.read_until(hostname.encode('ascii')+b'#')
    tn.write("show run".encode('ascii') + b"\n")
    aa = tn.read_until(hostname.encode('ascii')+b'#')
    #print(aa.decode('ascii'))

    aa1="C:\\tt\\"+hostname+".txt"
#    with open("C:\\luo.txt",'a+') as ff:
    with open(aa1,'a+') as ff:
        ff.write(aa.decode('ascii'))
        ff.write("exit%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    tn.write(b"exit\n")
    #print("exit")


def multitelnet():


 try:
    pool=multiprocessing.Pool(processes=4)
    f=open("C:\\12345.txt","r")
    num=1
    multipro=[]
    while True:
        line=f.readline().strip('\n')
        if line:
            argu=line.split('\t')
            #print (argu[0])
            #print (argu[1])
            print( '第'+str(num)+'个进程已启动')
            num+=1
            pool.apply_async(telnet,(argu[0],argu[1]))
        #    multipro.append(t)
        #    t.start()
        #    t.join()
        #    print( '第'+str(num)+'个进程已启动')
        #    num+=1
        else:
            break
    f.close()
    pool.close()
    pool.join()
    print ("Sub-process(es) done")
   # for j in multipro:
   #     j.start()
   #     j.join()
   #     print( '第'+str(num)+'个进程已启动')
   #     num+=1
 except Exception as  e:
   print (e)




if __name__ == "__main__" :
	multitelnet()
	# telnet("172.25.11.2",b"mpls-vrf-PE1")
