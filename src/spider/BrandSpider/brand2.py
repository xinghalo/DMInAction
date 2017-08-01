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
					index = self.getMaxPage(realThirdCategoryContent)

					# 解析当前页
					realThridCategoryItems = self.resolveLastPage(realThirdCategoryContent)

					for realThirdCategoryItem in realThridCategoryItems:
						brandCategory = realThirdCategoryItem[1] # 名称

						aboutContent = self.getPageContext('https:'+str(realThirdCategoryItem[0]))
						aboutItems = self.resolveAboutPage(aboutContent)

						brandContent = self.getPageContext('https:'+str(aboutItems))
						
						info = self.resolveBrandField(brandContent)
						
						print info[0],',',info[1],',',info[2],',',info[3],',',info[4],',',info[5],',',info[6],',',info[7],',',info[8],',',info[9],',',info[10],',',info[11],',',info[12]
	
	def resolveDan(self,content):
		try:
			pattern = re.compile('.*?<p><font color="#4993F4">主体规模：</font>(.*?)</p>.*?')
			return re.findall(pattern,content)[0]
		except:
			return 'null'

	def resolveZhuTiGuiMo(self,content):
		try:
			pattern = re.compile('.*?<p><font color="#4993F4">主体规模：</font>(.*?)</p>.*?')
			return re.findall(pattern,content)
		except:
			return 'null'

	def resolveBrandField(self,content):
		zhutiguimo = 'null'
		danweixingzhi = 'null'
		zichanleixing = 'null'
		chuangjianshijian = 'null'
		boss = 'null'
		address = 'null'
		zizhirongyu = 'null'
		score = 0
		price = 'null'
		rank = 'null'
		sales = 'null'
		renqi = 'null'

		try:
			pattern = re.compile('.*?<p style="height: 30px;line-height: 20px;">(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				name = result[0]

			pattern = re.compile('.*?<p><font color="#4993F4">主体规模：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				zhutiguimo = result[0]

			pattern = re.compile('.*?<p><font color="#4993F4">单位性质：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				danweixingzhi = result[0]
			
			pattern = re.compile('.*?<p><font color="#4993F4">资产类型：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				zichanleixing = result[0]

			pattern = re.compile('.*?<p><font color="#4993F4">成立于：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				chuangjianshijian = result[0]

			pattern = re.compile('.*?<p><font color="#4993F4">创办人、主要负责人或法人：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				boss = result[0]

			pattern = re.compile('.*?<p><font color="#4993F4">发源地或总部所在地：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				address = result[0]

			pattern = re.compile('.*?<p class="x"><span>*</span><font color="#4993F4">资质荣誉：</font>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				zizhirongyu = result[0]
			
			# <p class="zf">总分：92分</p>
			pattern = re.compile('.*?<p class="zf">总分：(.*?)分</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				score = result[0]

			# <p>综合排名：第<b style="color:#F60;" _hover-ignore="1">193</b>位</p>
			pattern = re.compile('.*?<p>综合排名：第<b style="color:#F60;">(.*?)</b>位</p>.*?')
			result = re.findall(pattern,content)
			if len(result) >0 :
				rank = result[0]

			# <p>品牌价值：<a href="//jiazhi.paizi.com/s?keys=惠普" style="color:#F60; font-weight:bold;" target="_blank">41832</a>百万元
			pattern = re.compile('.*?<p>品牌价值：<a href=".*?" style="color:#F60; font-weight:bold;" target="_blank">(.*?)</a>(.*?).*?')
			result = re.findall(pattern,content)
			if len(result) == 2 :
				price = str(result[0],result[1])
	
			# <p>估算销量：<b style="color:#F60;">4831</b>件/月</p>
			pattern = re.compile('.*?<p>估算销量：<b style="color:#F60;">(.*?)</b>(.*?)</p>.*?')
			result = re.findall(pattern,content)
			if len(result) == 2 :
				sales = str(result[0],result[1])

			# <p>品牌人气：<em id="zs_pprq">222811</em>
			pattern = re.compile('.*?<p>品牌人气：<em id="zs_pprq">(.*?)</em>.*?')
			result = re.findall(pattern,content)
			if len(result) > 0 :
				renqi = result[0]

			return [name,zhutiguimo,danweixingzhi,zichanleixing,chuangjianshijian,boss,address,zizhirongyu,score,price,rank,sales,renqi]
		except:
			print '解析品牌属性出错'
			return []

	def resolvePageName(self,content):
		try:
			pattern = re.compile('.*?<p style="height: 30px;line-height: 20px;">(.*?)</p>.*?')
			return re.findall(pattern,content)
		except:
			print '解析品牌页面出错'
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
			pattern = re.compile('.*?<p>名称：<a href="(.*?)">(.*?)</a></p>.*?')
			return re.findall(pattern,content)
		except:
			print "解析出错"
			return []	

	def resolveAboutPage(self,content):
		try:
			pattern = re.compile('.*?<a href="(.*?)">关于.*?')
			return re.findall(pattern,content)[0]
		except:
			return []

spider = Spider()
spider.run()