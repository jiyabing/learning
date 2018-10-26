import requests
from bs4 import BeautifulSoup
import json
import time
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


def position_detail(position_id):
    # 职位详情页url
    url = 'https://www.lagou.com/jobs/%s.html' % position_id
    headers = {
        'User-Agent': random.choice(UAList)['User-Agent'],
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'Upgrade-Insecure-Requests': '1',
    }
    res = requests.get(url, headers=headers)
    res.encoding = 'utf-8'
    html = res.text
    try:
        soup = BeautifulSoup(html, 'html.parser')
        position_description = soup.select('.job_bt')[0].text
        print(position_description)
    except:
        return ''
    return position_description


def main():
    headers = {
        'User-Agent': random.choice(UAList)['User-Agent'],
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'X-Anit-Forge-Code': '0',
        'X-Anit-Forge-Token': None,
        'X-Requested-With': 'XMLHttpRequest',

    }
    # url = 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='

    positions = []  # 30页所有职位
    # 真正有数据的url
    url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E6%AD%A6%E6%B1%89&needAddtionalResult=false'

    # 获取30页的数据(会出错，拉勾网做了限制)
    for i in range(1, 31):
        # 注意：请求为post请求,请求数据为form_data(可在F12中找到)
        form_data = {
            'first': 'true',
            'pn': i,  # 页数
            'kd': 'python',
        }
        res = requests.post(url, headers=headers, data=form_data)
        res.encoding = 'utf-8'
        dic = json.loads(res.text)

        # 每页中的职位
        page_positions = dic['content']['positionResult']['result']
        print(page_positions)

        # 获取职位信息
        for position in page_positions:
            # 拿到所需要的信息，保存在字典中
            position_dict = {
                'position_name': position['positionName'],
                'work_year': position['workYear'],
                'salary': position['salary'],
                'district': position['district'],
                'company': position['companyFullName']
            }

            # 职位id,用于访问详情页
            position_id = position['positionId']
            # 获取职位详细信息
            position_description = position_detail(position_id)
            # 将详细信息添加到字典中
            position_dict['position_description'] = position_description

            positions.append(position_dict)
            # time.sleep(3)

        time.sleep(3)

    print(positions)


if __name__ == '__main__':
    main()
    # position_detail(3448313)
