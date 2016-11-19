#coding=utf-8 
# 导入模块 urllib2                                                                                                      
import urllib.request, urllib.error, urllib.parse                                                                                                          
                                                                                                                        
# 随便查询一篇文章，比如On random graph。对每一个查询google                                                             
# scholar都有一个url，这个url形成的规则是要自己分析的。                                                                 
query = '邓肯'                                                                                               
url = 'https://www.baidu.com/s?wd=' + query + '&rsv_spt=1&rsv_iqid=0xd5bafc8d0002905c&issp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg&rsv_enter=1&rsv_sug3=1'                             
# 设置头文件。抓取有些的网页不需要专门设置头文件，但是这里如果不设置的话，                                              
# google会认为是机器人不允许访问。另外访问有些网站还有设置Cookie，这个会相对复杂一些
# 这里暂时不提。关于怎么知道头文件该怎么写，一些插件可以看到你用的浏览器和网站交互的                                    
# 头文件（这种工具很多浏览器是自带的），我用的是firefox的firebug插件。                                                  
header = {'Host': 'www.baidu.com',                                                                                 
'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:49.0) Gecko/20100101 Firefox/49.0',                                      
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',                                            
'Accept-Encoding': 'gzip, deflate',                                                                                     
'Connection': 'keep-alive'}  
print(header)                                                  
# 建立连接请求，这时google的服务器返回页面信息给con这个变量，con是一个对象                                              
req = urllib.request.Request(url, headers = header)       
print("req**=",req)                                                                  
#con = urllib.request.urlopen( req )  
#print("con**=",con)                                                                                          
# 对con这个对象调用read()方法，返回的是html页面，也就是有html标签的纯文本                                               
doc = req.read()                                                                                                        
# 关闭连接。就像读完文件要关闭文件一样，如果不关闭有时可以、但有时会有问题，                                            
# 所以作为一个守法的好公民，还是关闭连接好了。
#print(doc)                                                                          
con.close()                                                                                                             