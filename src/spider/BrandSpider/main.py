#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re

url = 'http://brand.efu.com.cn/'
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
headers = { 'User-Agent' : user_agent }
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
content = response.read()
pattern = re.compile('.*?<h2><a title="(.*?)" href="http.*?</a></h2>.*?')
items = re.findall(pattern,content)
for item in items:
	# print 1
	print item
print "结束"
