import requests
import urllib.request, urllib.error
import os
import time
import threading
from bs4 import BeautifulSoup


BASE_PAGE_URL = 'https://www.doutula.com/photo/list/?page='
# 页面url列表
PAGE_URL_LIST = (BASE_PAGE_URL + str(i) for i in range(1, 6))
# 图片url列表
IMAGE_URL_LIST = []
# 全局锁
gLock = threading.RLock()
# for x in range(1, 1001):
#     PAGE_URL_LIST.append(BASE_PAGE_URL + str(x))


def download_image():
    # 下载图片，指定路径和图片名
    # https://ws1.sinaimg.cn/bmiddle/9150e4e5gy1fugn0w7v18j20hr0hs3zu.jpg
    while True:
        gLock.acquire()
        if len(IMAGE_URL_LIST) == 0:
            gLock.release()
            # continue
            print('下载完成')
            return
        else:
            url = IMAGE_URL_LIST.pop()
            gLock.release()
            filename = url.split('/').pop()
            # 指定图片保存路径
            path = os.path.join('images', filename)
            try:
                urllib.request.urlretrieve(url, path)
            except :
                continue
        # time.sleep(1)


def get_image_url():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\ '
                      'AppleWebKit/537.36 (KHTML, like Gecko)\ '
                      'Chrome/68.0.3440.106 Safari/537.36'
    }
    while True:
        gLock.acquire()
        try:
            url = next(PAGE_URL_LIST)
            gLock.release()
        except StopIteration:
            gLock.release()
            return
        res = requests.get(url, headers=headers)
        res.encoding = 'utf-8'
        html = res.text
        soup = BeautifulSoup(html, 'html.parser')
        img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
        # gLock.acquire()
        for img in img_list:
            # 获取图片url
            img_url = img['data-backup'][:-4]
            # if img_url.endswith('!dta'):
            #     img_url = img_url[:-4]
            gLock.acquire()
            IMAGE_URL_LIST.append(img_url)
            gLock.release()
        # print(len(IMAGE_URL_LIST))
        # gLock.release()

        # 设置一段时间，防反爬
        time.sleep(3)


def main():
    # 创建3个线程进行获取图片url
    for i in range(3):
        th = threading.Thread(target=get_image_url)
        th.start()
    time.sleep(2)
    # 创建5个线程进行图片下载
    for i in range(5):
        th = threading.Thread(target=download_image)
        th.start()


if __name__ == '__main__':
    main()
