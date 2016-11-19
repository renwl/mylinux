#coding=utf-8
import urllib.request, urllib.parse, urllib.error
import re
import time

def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html

def getImg(html):
	reg = r'src="(.+?\.jpg)" pic_ext'
	imgre = re.compile(reg)
	html=html.decode("utf-8","ignore")
	imglist = re.findall(imgre,html)
	x = 0
	for imgurl in imglist:
		print("list=",imgurl)
		time.sleep(1)
		urllib.request.urlretrieve(imgurl,r'e:\%s.jpg' % x)
		x+=1
		
		
html = getHtml("http://tieba.baidu.com/p/2460150866")

print(getImg(html))