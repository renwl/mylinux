#coding=utf-8   
#http://www.tuicool.com/articles/V36vyuJ
#Python3学习笔记（urllib模块的使用）
from urllib import request, parse
url = r'http://www.lagou.com/jobs/positionAjax.json?'
def get_page(url):
	headers = {
	    'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
	                r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
	    'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
	    'Connection': 'keep-alive'
	}
	data = {
	        'first': 'true',
	        'pn': 1,
	        'kd': 'Python'
	    }
	proxy = request.ProxyHandler({'http': '5.22.195.215:80'})  # 设置proxy
	opener = request.build_opener(proxy)  # 挂载opener
	request.install_opener(opener)  # 安装opener
	data = parse.urlencode(data).encode('utf-8')
	page = opener.open(url, data).read()
	page = page.decode('utf-8')
	return page                                     
page=get_page(url)
print("page=",page)