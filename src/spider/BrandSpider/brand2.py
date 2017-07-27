#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import json

class Spider:

	def __init__(self):
		self.url = 'https://www.paizi.com/'
		self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
		self.headers = { 'User-Agent' : self.user_agent }
	
	def getBrandCategory(self):
		content = self.getPageContext(self.url)
		indexItems = self.resolveIndexContent(content)
		for indexItem in indexItems:
			firstCategory = indexItem[1]
			
			firstCategoryContent = self.getPageContext('https:'+str(indexItem[0]))
			firstCategoryItems = self.resolveFirstCategoryContent(firstCategoryContent)

			for firstCategroyItem in firstCategoryItems:
				sencondCategory = firstCategroyItem[1]

				secondCategoryContent = self.getPageContext('https:'+str(firstCategroyItem[0]))
				secondCategoryItems = self.resolveSecondCategoryContent(secondCategoryContent)

				for secondCategoryItem in secondCategoryItems:

					thirdCategory = secondCategoryItem[1]

					thirdCategoryContent = self.getPageContext('https:'+str(secondCategoryItem[0]))
					realUrl = self.getRealUrl(thirdCategoryContent)
					realThirdCategoryContent = self.getPageContext('https:'+str(realUrl))
					# print realUrl
					index = self.getMaxPage(realThirdCategoryContent)

					# 解析当前页

					realThridCategoryItems = self.resolveLastPage(realThirdCategoryContent)

					for realThirdCategoryItem in realThridCategoryItems:
						print realThirdCategoryItem[0]
						print realThirdCategoryItem[1]

					# if index > 0:
					# 	for i in range(1,index):
					# 		lastPageContent = self.getPageContext('https:'+str(realUrl[:-5]+'-'+i+'.html'))
					
		

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
	
	def resolveIndexContent(self,content):
		try:
			pattern = re.compile('.*?<h3><em></em><a href="(.*?)">(.*?)</a></h3>.*?')
			return re.findall(pattern,content)
		except:
			# print '忽略解析品牌页面出错问题'
			return []		

	def resolveFirstCategoryContent(self,content):
		try:
			pattern = re.compile('.*?<div class="con06">([\s\S]*?)<div class="con07">.*?')
			div = re.findall(pattern,content)
			pattern = re.compile('.*?<strong><a href="(.*?)">(.*?)</a></strong>.*?')
			return re.findall(pattern,div[0])
		except:
			# print '忽略解析品牌页面出错问题'
			return []

	def resolveSecondCategoryContent(self,content):
		try:
			pattern = re.compile('.*?<div class="c-3">([\s\S]*?)</div>.*?')
			div = re.findall(pattern,content)
			pattern = re.compile('.*?<a href="(.*?)">(.*?)</a>.*?')
			return re.findall(pattern,div[0])
		except:
			# print '忽略解析品牌页面出错问题'
			return []	

	def getRealUrl(self,content):
		try:
			pattern = re.compile('.*?<a href="(.*?)">.*?品牌大全></a>.*?')
			return re.findall(pattern,content)[0]
		except:
			print "解析出错"
			return []	

	def getMaxPage(self,content):
		# <div class="pages clear"><a class="a1">182条</a> <a href="d5802.html" class="a1">上一页</a> <span>1</span> <a href="d5802-2.html">2</a> <a href="d5802-3.html">3</a> <a href="d5802-4.html">4</a> <a href="d5802-5.html">5</a> ..<a href="d5802-7.html">7</a> <a href="d5802-2.html" class="a1">下一页</a></div>
		try:
			pattern = re.compile('.*?\.\.<a href=".*?">(\d)</a>.*?')
			index = re.findall(pattern,content)
			if len(index) == 0:
				return 0
			else:
				return index[0]
		except:
			print "获取最大值出错"
			return []

	def resolveLastPage(self,content):
		# <div class="c03"><p>名称：<a href="
		try:
			pattern = re.compile('.*?<div class="c03"><p>名称：<a href=".*?">(.*?)</a></p><p>口碑：.*?<a class="c07" href="(.*?)">\> 详情</a>.*?')
			return re.findall(pattern,content)
		except:
			print "解析出错"
			return []	

spider = Spider()
spider.run()