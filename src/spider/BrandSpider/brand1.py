#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import json

class Spider:

	def __init__(self):
		self.url = 'http://brand.efu.com.cn/'
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		self.headers = { 'User-Agent' : self.user_agent }
	
	def getBrandCategory(self):

		f = open('brand1.csv','a')
		f.write('品牌,目标消费群体,分类\n')
		f.close()

		content = self.getPageContext(self.url)
		items = self.resolveIndexContent(content)

		for line in items:
			context = [line[0]]
			# 循环遍历每一个分类下的页码
			url = line[1]
			for num in range(1,1000):
				nexturl = self.url+url[:-6]+str(num)+".html" # 拼接每一页的url
				pageContent = self.getPageContext(nexturl) # 爬取分页的内容

				# 判断此页是否有内容
				if pageContent.find('<div class="lstPhotob">') == -1:
					break
				
				# 处理分页页面内容
				pageItems = self.resolvePageContent(pageContent,context[0])

				if len(pageItems) == 0:
					break

				
				for pageLine in pageItems:
					# print pageLine[0]
					# print pageLine[1]
					brandContent = self.getPageContext(pageLine[0])
					brandItems = self.resolveBrandContext(brandContent)

					if len(brandItems) == 0:
						break

					f = open('brand1.csv','a')
					for brandLine in brandItems:
						if brandLine[0] == '目标消费群体':
							output = str(pageLine[1])+","+str(brandLine[1])+","+str(line[0])
							print output
							f.write(output)
							f.write("\n")
							break
					f.close()

		
	def resolveBrandContext(self,content):
		# [\s\S]+?
		try:
			pattern = re.compile('.*?<span class="sp-a">(.*?)</span>.*?<span class="sp-b">(.*?)</span>.*?')
			return re.findall(pattern,content)
		except:
			# print '忽略解析品牌页面出错问题'
			return []

	def resolveIndexContent(self,content):
		try:
			pattern = re.compile('.*?<li><a  title="(.*?)" href="(.*?)">.*?</a></li>.*?')
			return re.findall(pattern,content)
		except:
			# print '忽略解析首页出错问题'
			return []

	def resolvePageContent(self,content,category):
		# pattern = re.compile('.*?<div class="lstPhotob"><div class="lstPa"><div class="lstPa-a"><a href="(.*?)" target="_blank" title="(.*?)>.*?')
		try:
			pattern = re.compile('.*?<a href="(.*?)" target="_blank" title="(.*?)'+category+'品牌">.*?')
			return re.findall(pattern,content)
		except:
			# print '忽略解析分页页面出错问题'
			return []

	def getPageContext(self,url):
		# print '爬取页面',url
		try:
			request = urllib2.Request(url,headers = self.headers)
			response = urllib2.urlopen(request)
			return response.read()
		except:
			1
			# print '忽略url发送出错问题'

	def run(self):
		self.getBrandCategory()
		


spider = Spider()
spider.run()