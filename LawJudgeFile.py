# -*- coding: gbk -*-
#�����ǵ���ģ�飬���������вˡ�ϴ�롢����һ�������·ֱ��ץȡ��ҳ�����ݴ����桢ʱ�䡢������ʽ�� 
import urllib.request as req 
import pandas as pd 
import time 
import re 
#ͨ��F12���ҵ���POST��ҳ 
url='http://wenshu.court.gov.cn/List/ListContent' 
#����ҳ������Ϣʱ��Ķ���������յ��б�����װɸѡ������ݡ� 
Index=1 
SleepNum = 3 
dates=[] 
titles=[] 
nums=[] 
#ѭ��ģ�飬��Ϊ�кܶ�ҳ����С�������ʱ�����ϵĴ����ݣ��൱�ڵ���һҳ�Ĺ��ܣ����һ�����˼��ÿִ��һ�Σ�index��1������ҳ��Ҳ�����ñ���ʵ�֣��������� 
while Index<123: 
	#��������ͷ��αװ�������������վ 
	my_headers={'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.95 Safari/537.36 Core/1.50.1280.400',} 
	#��һ�бȽ���Ҫ��������������Ҳ��ͨ��F12���ҵ�FORMDATA�ĸ�ʽ���У���������ϸ˵�� 
	data={'Param':'��Ժ����:****', 'Index': Index,'Page':'20','Order':'��������','Direction':'asc'}
	#����ַ������ͷ��Ҫpost�������ϴ� 
	r=req.Request(url, headers=my_headers, data = data)
	#ȡ�õ�������json����ıȽϺã�textҲ�����ˣ�������Ϊʲô����Ҳ��֪���� 
	print(dir(r))
	raw=r.decode("utf-8","ignore") 
	#��ץȡ�µ�������������ʽ��������Ҫ��������ȡ������������ʽ��ĺ����ã�Ҫ���ú�westlaw֮������ݿ⣬��һ��Ҳ�ùء� 
	#�����Ƕ���ɸѡ��׼���ѣ����������ڡ������󣬣�'��ǰ�����ݽ�ȡ������ 
	pattern1 = re.compile('"��������":"(.*?)"', re.S) 
	date = re.findall(pattern1,raw) 
	pattern2 = re.compile('"����":"(.*?)"', re.S) 
	num = re.findall(pattern2,raw) 
	pattern3 = re.compile('"��������":"(.*?)"', re.S) 
	title = re.findall(pattern3,raw) 
	#��ɸѡ����������ӵ���ʼ���������б��� 
	dates+=date 
	titles+=title 
	nums+=num 
	#��һ�����ó�����Ϣ������������رȽϺá�ͨ��ץȡ����ҳ��ܿ�֪��������������֤�빦�ܵģ������ץ��̫������Ī�֡� 
	time.sleep(SleepNum) 
	Index += 1 
	#��pandasģ�齫ɸѡ��������ת��dataframe��ʽ�������浽Excel�� 
	df=pd.DataFrame({'ʱ��':dates,'����':nums, '��������':titles}) 
	df.to_excel('C:\\result.xlsx')