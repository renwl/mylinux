# -*- coding: gbk -*-
#这里是导入模块，就像招人切菜、洗碗、炒菜一样，以下分别管抓取网页、数据处理保存、时间、正则表达式。 
import urllib.request as req 
import pandas as pd 
import time 
import re 
#通过F12查找到的POST网页 
url='http://wenshu.court.gov.cn/List/ListContent' 
#这是页数、休息时间的定义和三个空的列表用来装筛选后的数据。 
Index=1 
SleepNum = 3 
dates=[] 
titles=[] 
nums=[] 
#循环模块，因为有很多页，当小于这个数时，不断的传数据，相当于点下一页的功能，最后一句的意思是每执行一次，index加1。具体页数也可以用变量实现，但我懒。 
while Index<123: 
	#这是请求头，伪装成浏览器访问网站 
	my_headers={'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.95 Safari/537.36 Core/1.50.1280.400',} 
	#这一行比较重要，是搜索条件，也是通过F12查找到FORMDATA的格式才行，具体下文细说。 
	data={'Param':'法院名称:****', 'Index': Index,'Page':'20','Order':'裁判日期','Direction':'asc'}
	#将网址、请求头、要post的数据上传 
	r=req.Request(url, headers=my_headers, data = data)
	#取得的数据用json翻译的比较好，text也看得了，别问我为什么，我也不知道。 
	print(dir(r))
	raw=r.decode("utf-8","ignore") 
	#对抓取下的内容用正则表达式将我们需要的内容提取出来，正则表达式真的很有用，要想用好westlaw之类的数据库，这一关也得关。 
	#大意是定义筛选标准，把（“裁判日期”：）后，（'）前的内容截取出来。 
	pattern1 = re.compile('"裁判日期":"(.*?)"', re.S) 
	date = re.findall(pattern1,raw) 
	pattern2 = re.compile('"案号":"(.*?)"', re.S) 
	num = re.findall(pattern2,raw) 
	pattern3 = re.compile('"案件名称":"(.*?)"', re.S) 
	title = re.findall(pattern3,raw) 
	#把筛选出的数据添加到开始的三个空列表里 
	dates+=date 
	titles+=title 
	nums+=num 
	#这一行是让程序休息，做事留点余地比较好。通过抓取的网页框架可知，文书网是有验证码功能的，如果你抓的太狠中招莫怪。 
	time.sleep(SleepNum) 
	Index += 1 
	#用pandas模块将筛选出的内容转成dataframe格式，并保存到Excel。 
	df=pd.DataFrame({'时间':dates,'案号':nums, '案件名称':titles}) 
	df.to_excel('C:\\result.xlsx')