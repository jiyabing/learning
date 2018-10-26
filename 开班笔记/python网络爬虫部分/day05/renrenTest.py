# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 15:01:40 2018

@author: jyb
"""

import urllib

# 这里的url是每个人自己的主页
url = 'http://www.renren.com/966952925/profile'
# header里面需要一个cookie,
# 这里的cookie需要你首先登录人人网，
# 然后在抓包工具中提取出这个cookie

header = {'Connection':'keep-alive',
          'Cookie':'anonymid=jjnxp0523vbb20; depovince=HUB; _r01_=1; ick_login=1adbaf39-9416-4a94-a5bd-9c6347d83611; t=9bbcf9e21d9976084e1297091d02752f5; societyguester=9bbcf9e21d9976084e1297091d02752f5; id=966952925; xnsid=5e0e42b0; jebecookies=13f324d1-ab82-414d-ba65-e9502a4dc444|||||; JSESSIONID=abcLK9tK3TdFp432B8Hsw; jebe_key=0d7fd19b-ff4a-43e8-9c98-520a95b3b98a%7C78311d7c3b50ab7761f8db40ee4f2ecd%7C1531725335751%7C1%7C1531725340389; wp_fold=0',
          'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
          'Host':'www.renren.com'}
req = urllib.request.Request(url, headers=header)
response = urllib.request.urlopen(req)

with open('myrenren.html', 'wb') as f:
    f.write(response.read())