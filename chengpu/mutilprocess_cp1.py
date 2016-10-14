__author__ = 'caohuan'
import telnetlib
import multiprocessing

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
    print(aa.decode('ascii'))
    tn.write(b"exit\n")
    print("exit")

def multitelnet():

 pool=multiprocessing.Pool(processes=128)
 try:
    f=open("C:\\123 - Copy.txt","r")
    num=1
    multipro=[]
    while True:
        line=f.readline().strip('\n')
        if line:
            argu=line.split('\t')
            t=multiprocessing.Process(target=telnet,args=(argu[0],argu[1]))
            multipro.append(t)
        #    t.start()
        #    t.join()
        #    print( '第'+str(num)+'个进程已启动')
        #    num+=1
        else:
            break
    f.close()

    for j in multipro:
        j.start()
        j.join()
        print( '第'+str(num)+'个进程已启动')
        num+=1
 except Exception as  e:
   print (e)




if __name__ == "__main__" :
	multitelnet()
	# telnet("172.25.11.2",b"mpls-vrf-PE1")
