# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:03:16 2018

@author: jyb
"""

import requests
from urllib import request
import random
UAList = [
                {"User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                {"User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"},
                {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)"},
                {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
                {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"},
                {"User-Agent": "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11"},
                {"User-Agent": "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11"},
                {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)"},
                {"User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)"},            
            ]
#headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
#print(request.urlopen(request.Request(
#        'http://www.sina.com.cn',
#        headers=random.choice(UAList))).read().decode('utf8'))

##TODO：
##思考：在requests中如何修饰headers.

#print(requests.get('http://www.sina.com.cn').text)
for _ in range(10):
    header = random.choice(UAList)
    print(header)
    res = requests.get('http://www.sina.com.cn', headers=header)
    res.encoding = 'utf-8'
#    print(res.text)
    #打印状态码
    print(res.status_code)

##TODO：
##思考，除了状态码之外是否还有其他方法来判断

#汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a,'-->',c)
        return
    else:
        move(n-1, a, c, b)#将n-1个圆盘移动到b
        move(1, a, b, c)#将a的最后一个圆盘移动到c
        move(n-1, b, a, c)#在将b的n-1个圆盘移动到c

#move(64, 'A', 'B', 'C')

#递归优化，以斐波那契数列为例
def fab2(n):
    # 给斐波那契数列的前两个元素赋初值
    # 同时利用index记录循环进行的下标位置
    index, a, b = 0, 1, 1
    while index < n-2:
        a, b = b, a+b
        index += 1
    return b
##TODO：
##思考？？？，用yield实现
