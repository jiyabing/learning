# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 11:31:53 2018

@author: Administrator
"""

import urllib
from urllib import request
import re

#urllib.parse.urlencode()

# 完成一次get请求
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
url = "https://www.baidu.com/s?"
keyword = input("请输入您要查询的信息:")
wd = {"wd":keyword}
wd = urllib.parse.urlencode(wd) #url encode 编码
fullUrl = url+wd
#print(fullUrl) #https://www.baidu.com/s?wd=Python%E7%88%AC%E8%99%AB

# 获取到get请求的信息，写文件
req = request.Request(fullUrl,headers=headers)
response = request.urlopen(req)
html = response.read()
#html = response.read().decode('utf-8')
#print(html)
with open("baiduSearch.html", "wb") as f:
    f.write(html)

# 正则表达式来获取百度搜索推荐的信息
pattern = re.compile('<div><a target="_blank" href=([\s\S]*?)>([\s\S]*?)</a>')
items = re.findall(pattern, html.decode('utf-8'))
with open("baiduSearch.txt", 'a') as f:
    for it in items:
        print(it[0], it[1])
        f.write("推荐: "+it[1]+"链接: "+it[0]+"\n")
        
        
        
        
        
        
        
        
        
        
