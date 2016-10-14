import json

def processJson(input,output):
    fin=open(input,'r')
    fout=open(output,'w')
    js=json.load(fin)
    print(js)
    js["user"]='luozt'
    outstr=json.dumps(js,ensure_ascii=False)+','
    fout.write(outstr.strip()+'\n')
    fin.close()
    fout.close()


if __name__=='__main__':
    processJson('D:\\search\\bb\\fix_RMConfig.json','D:\\search\\bb\\fix_RMConfig1.json')