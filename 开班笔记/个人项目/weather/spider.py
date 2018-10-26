import requests
from bs4 import BeautifulSoup
from pyecharts import Bar

ALL_DATA = []


def parser_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ '
                      'AppleWebKit/537.36 (KHTML, like Gecko)\ '
                      'Chrome/68.0.3440.106 Safari/537.36',
        'Host': 'www.weather.com.cn',
        'Upgrade-Insecure-Requests': '1'
    }
    response = requests.get(url, headers=headers)
    # response.content返回的是二进制数据，需要进行解码
    html = response.content.decode('utf8')
    # 对html进行解析,html5lib解析较慢
    soup = BeautifulSoup(html, 'html5lib')
    # 获取相应的数据
    conMidtab = soup.find('div', {'class': 'conMidtab'})
    # 找到当前页面上所有省/直辖市
    provinces = conMidtab.find_all('table')
    for province in provinces:
        # 找出当前省/直辖市下的所有城市
        cities = province.find_all('tr')[2:]
        for city in cities:
            # 每个城市下的天气所有信息
            details = city.find_all('td')
            # 取出需要的信息存入字典中
            weather = dict()
            weather['city_name'] = details[-8].text.strip()
            if details[-5].text == '-':
                weather['max_temp'] = 0
            else:
                weather['max_temp'] = int(details[-5].text)
            if details[-2].text == '-':
                weather['min_temp'] = 0
            else:
                weather['min_temp'] = int(details[-2].text)
            ALL_DATA.append(weather)
            # print(weather)


def main():
    urls = [
        'http://www.weather.com.cn/textFC/hb.shtml',
        'http://www.weather.com.cn/textFC/db.shtml',
        'http://www.weather.com.cn/textFC/hz.shtml',
        'http://www.weather.com.cn/textFC/hd.shtml',
        'http://www.weather.com.cn/textFC/hn.shtml',
        'http://www.weather.com.cn/textFC/xb.shtml',
        'http://www.weather.com.cn/textFC/xn.shtml',
        'http://www.weather.com.cn/textFC/gat.shtml'
    ]
    for url in urls:
        parser_page(url)

    # 按最高温进行排序
    ALL_DATA.sort(key=lambda dic: dic['max_temp'])
    # print(ALL_DATA)
    # 取出前十
    Top10 = ALL_DATA[-1:-11:-1]
    cities = list(map(lambda x: x['city_name'], Top10))
    temp = list(map(lambda x: x['max_temp'], Top10))
    # 绘制图表
    charts = Bar('中国高温前十排行榜', '单位：℃')
    charts.use_theme('dark')
    charts.add('高温', cities, temp, is_more_utils=True)
    charts.render('temperature.html')


if __name__ == '__main__':
    main()
