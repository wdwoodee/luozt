from suds.client import Client

url = r'http://10.10.5.123/workspace/1/nbws3rdparty.asmx?wsdl'
client = Client(url)
print client

