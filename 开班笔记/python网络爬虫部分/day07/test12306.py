# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:30:14 2018

@author: Python
"""

import urllib
import ssl
#https = http+ssl(安全套接层)

# 手动的增加授信
# Create a SSLContext object
context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"
ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

# HTTP Request
req = urllib.request.Request(url,
                             headers=ua_headers)
# HTTP Response
response = urllib.request.urlopen(req, 
                       context=context)

with open("12306.html", "wb") as f:
    f.write(response.read())
#CertificateError:

