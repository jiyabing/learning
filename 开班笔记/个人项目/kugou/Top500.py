import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

# 连接数据库
client = MongoClient()
songs = client.kugou_db.songs


def get_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ '
                      'AppleWebKit/537.36 (KHTML, like Gecko)\ '
                      'Chrome/68.0.3440.106 Safari/537.36',
        'Host': 'www.kugou.com',
        'Upgrade-Insecure-Requests': '1'
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'
    html = resp.text
    soup = BeautifulSoup(html, 'lxml')
    # 获取排名
    ranks = soup.select('.pc_temp_num')
    # 获取歌名和歌手
    titles = soup.select('.pc_temp_songname')
    # 获取时间长度
    times = soup.select('.pc_temp_time')
    for rank, title, time in zip(ranks, titles, times):
        detail = title.text
        # 对没有歌手名的进行相应处理
        if '-' not in detail:
            detail = detail + '- unknown'
        data = {
            'rank': rank.text.strip(),
            'name': detail.split('-')[1].strip(),
            'singer': detail.split('-')[0].strip(),
            'time': time.text.strip()
        }
        print(data)
        song_id = songs.insert(data)
        print(song_id)


if __name__ == '__main__':
    base_url = 'http://www.kugou.com/yy/rank/home/{}-8888.html?from=rank'
    urls = [base_url.format(str(i)) for i in range(1, 24)]
    for url in urls:
        print(url)
        get_info(url)
        time.sleep(1)
