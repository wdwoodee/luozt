import os
path1='D:\\Qapp\\device.config'
if os.path.exists(path1):
    os.remove(path1)
with open(path1,'w') as f:

    for i in range(1,15001):
        f.write("Current configuration"+str(i)+" : 12292082 bytes"+"\n")
        f.write("  upgrade fpd"+str(i)+" auto"+"\n")
        f.write("  version 15.1v"+str(i)+"\n")
        f.write("  no service"+str(i)+" pad"+"\n")
        f.write("  service timestamps"+str(i)+" debug datetime msec localtime show-timezone"+"\n")
        f.write("  hostname bgl04-gem-wan-gw2"+str(i)+"\n")
        f.write("  boot system"+str(i)+" flash disk2:c7200p-adventerprisek9-mz.151-4.M4.bin"+"\n")
        f.write("  logging snmp-authfail"+str(i)+"\n")
        f.write("  no logging"+str(i)+" console"+"\n")
        f.write("  enable secret"+str(i)+" level 5 5 $1$D5p7$9.S4NIS8xWvN.nm8GC2Mw."+"\n")
        f.write("  aaa group"+str(i)+" server tacacs+ vty_access"+"\n")
        f.write("  server 72.163.128.165"+"\n")
        f.write("  clock timezone"+str(i)+" IST 5 30"+"\n")
        f.write("  ip domain name"+str(i)+" cisco.com"+"\n")
        f.write("  ip name-server"+str(i)+" 72.163.128.140"+"\n")
        f.write("  ip inspect name"+str(i)+" prgn1-in udp"+"\n")
        f.write("  ip wccp web-cache"+str(i)+" redirect-list wccp_redirectstandby password 7 073425794D0A09442A"+"\n")
        f.write("  crypto pki"+str(i)+" token default removal timeout 0"+"\n")
        f.write("  controller E1"+str(i)+" 3/0"+"\n")
        f.write("  framing NO-CRC4 "+str(i)+"\n")
        f.write("  pri-group timeslots"+str(i)+" 1-31"+"\n")
        f.write("************************************************************************************"+"\n")
