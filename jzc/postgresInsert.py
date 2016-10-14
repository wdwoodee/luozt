#_DEBUG = True

import psycopg2
import pdb

try:
    conn = psycopg2.connect(database="workspace2", user="postgres", password="postgres", host="127.0.0.1", port="54321")
except Exception:
    print('Get a exception: Connect failed')
    
print("successfully")
cur = conn.cursor()
try:
    errLine = 0
    with open("test1ip.csv") as f:
        i = 0
        while True:
            ln = f.readline()
            if not ln:
                break
            items = ln.split(',')
           
            if(items[0]=='LAN Segment'):
                continue       
           
            if len(items) != 13:
                errLine += 1
                continue
            
            #pdb.set_trace()
            if items[10] == "Device Interface":
                items[10]=9
            elif items[10] == "ARP Table":
                items[10]=7
            elif items[10] == "CDP/LLDP Table":
                items[10]=8
            elif items[10] == "MAC Table":
                items[10]=6
            elif items[10] == "Manual":
                items[10]=1
            else :
                items[10]=0

            #if ( not items[8].isnumeric()) or ( not items[10].isnumeric())  or ( not items[11].isnumeric())  :
            #    pdb.set_trace()
             #   errLine += 1
             #   continue

            try:
                sqlinsert = "select saveoneiprecode_ip2mac_x64 ( false, '%s', '%s', '', '%s',  '%s', '%s',  '%s', '%s', '%s', %s,  %s, %s)" % (items[9], items[0], items[1], items[2], items[4], items[5], items[6], items[7], items[8], items[10], items[11])
                cur.execute(sqlinsert)
            except Exception:
                print("Insert Err:%s",sqlinsert)
                errLine += 1
                continue

            i += 1

            if ( (i%5)==0 ):
                #pdb.set_trace()
                conn.commit()
    conn.commit()

    print ("Complete: insert %d , err %d" %( i, errLine) );
    conn.close() 

except Exception:
    print('Get a exception')
    
