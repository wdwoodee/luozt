__author__ = 'caohuan'
import telnetlib
import threading
import struct
import binascii
import time
def telnet(ip,hostname):
  try:
    #print ('call '+ip+'call '+hostname)
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
  except Exception as e:
      print (e)
def multitelnet():


 try:
    f=open("C:\\123","r")
    num=1
    threads=[]
    while True:
        line=f.readline().strip('\n')

        if line:
            argu=line.split('\t')
         #   print (argu[0])
         #   print (argu[1])
            t=threading.Thread(target=telnet,args=(argu[0],argu[1]))
            threads.append(t)
       #     t.start()
       #     print ('第'+num+'一个线程已启动')
        #    num+=1
        else:
            break
    f.close()

    for j in threads:
        j.start()
        print ('第'+str(num)+'一个线程已启动')
        num+=1
    for t in threads:
        t.join()
 except Exception as  e:
   print (e)




if __name__ == "__main__" :
	multitelnet()
	# telnet("172.25.11.2",b"mpls-vrf-PE1")
