#-*- coding: UTF-8 -*- 
import urllib
import urllib2
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

url = 'http://www.china-ef.com/brand/'
#url = 'http://www.baidu.com'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'  
#values = {'username' : 'cqc',  'password' : 'XXXX' }  
values = {}
headers = { 'User-Agent' : user_agent }  
data = urllib.urlencode(values)  
request = urllib2.Request(url,data,headers)  
response = urllib2.urlopen(request)
print response.read()