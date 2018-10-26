"""
主要使用多进程爬取
"""
import requests
import re
import time
from multiprocessing import Pool


def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ '
                      'AppleWebKit/537.36 (KHTML, like Gecko)\ '
                      'Chrome/68.0.3440.106 Safari/537.36',
        'Host': 'www.qiushibaike.com',
        'Referer': 'https://www.qiushibaike.com/',
        'Upgrade-Insecure-Requests': '1'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    names = re.findall('<h2>([\s\S]*?)</h2>', html, re.S)
    contents = re.findall('<div class="content">[\s\S]*?<span>([\s\S]*?)</span>', html, re.S)
    laughs = re.findall('<i class="number">([\s\S]*?)</i>', html, re.S)
    comments = re.findall('<span class="stats-comments">[\s\S]*?<i class="number">([\s\S]*?)</i>', html, re.S)
    info_list = []
    for name, content, laugh, comment in zip(names, contents, laughs, comments):
        info = {
            'title': name.strip(),
            'content': content.strip(),
            'laugh': laugh.strip(),
            'comment': comment.strip()
        }
        info_list.append(info)
    return info_list


if __name__ == '__main__':
    base_url = 'https://www.qiushibaike.com/8hr/page/{}/'
    urls = [base_url.format(str(i)) for i in range(1, 14)]
    # 串联执行
    # start1 = time.time()
    # for url in urls:
    #     get_info(url)
    # end1 = time.time()
    # print(end1 - start1)

    # 两个进程
    # start2 = time.time()
    # pool = Pool(processes=2)
    # pool.map(get_info, urls)
    # end2 = time.time()
    # print(end2 - start2)

    # 四个进程
    start3 = time.time()
    pool = Pool(processes=4)
    pool.map(get_info, urls)
    end3 = time.time()
    print(end3 - start3)
