# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 15:57:38 2018

@author: jyb
"""

# 抓取猫眼top100的数据
import requests
import re
import json
from multiprocessing import Pool
from multiprocessing import Manager
import time
import functools #函数包装器

# step1：下载页面
def get_one_page(url):
    # 设置UA
    ua_header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}
    res = requests.get(url, headers=ua_header)
    if res.status_code == 200: # OK
        return res.text
    return None

# step2：提取信息
def parse_one_page(html):
    #使用正则表达式懒惰+findall的模式
    pattern = re.compile('''<p class="name">[\s\S]*?title="([\s\S]*?)"
                         [\s\S]*?<p class="star">([\s\S]*?)</p>
                         [\s\S]*?<p class="releasetime">([\s\S]*?)</p>''')
    items = re.findall(pattern, html)
    for item in items:
        yield {
                "name": item[0].strip(),
                "star": item[1].strip(),
                "releasetime": item[2].strip(),
               }
    
# step3：保存到本地文件系统中
def write_to_file(item):
    # 存储成json格式，以便以后方便提取
    with open("maoyanTop100.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')

# 0-100: 0, 10, 20, ...,90
# http://maoyan.com/board/4?offset=90
def CrawlPage(lock, offset):
    # 将下载页面，解析页面及保存信息放入一个
    url = "http://maoyan.com/board/4?offset=" + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        lock.acquire() #加锁
        write_to_file(item)
        lock.release() #释放锁
    time.sleep(0.5)

 
if __name__ == "__main__":
    # 使用进程池来抓取数据
    # 在进程池之间通信或者加锁需要用Manager
    manager = Manager()
    lock = manager.Lock()
    # 产生一个新的包装函数
    newCrawlPage = functools.partial(CrawlPage, lock)
    pool = Pool()
    pool.map(newCrawlPage, [i*10 for i in range(10)])
    pool.close()
    pool.join()
    
    