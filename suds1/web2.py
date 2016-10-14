from suds.client import Client

url = r'http://10.10.5.102//com.netbrain.ng.webservices/ngapi?access_token='
client = Client(url)
print client
