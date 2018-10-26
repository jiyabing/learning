import sys

from selenium import webdriver
import time
from lxml import etree
from pymongo import MongoClient

client = MongoClient('127.0.0.1', 27017)
db = client['tb_db']
collection = db.get_collection('taobao')


def get_data(url, page):
    page += 1
    driver.get(url)
    driver.implicitly_wait(10)
    html = etree.HTML(driver.page_source)
    # with open('hello.html', 'w', encoding='utf-8') as f:
    #     f.write(driver.page_source)
    # print(html)
    infos = html.xpath('//div[@class="item J_MouserOnverReq  "]|//div[@class="item J_MouserOnverReq item-ad  "]')
    for info in infos:
        detail = info.xpath('.//div[@class="pic"]/a/img/@alt')[0]
        price = info.xpath('div[2]/div[1]/div[1]/strong/text()')[0]
        sell = info.xpath('div[2]/div[1]/div[@class="deal-cnt"]/text()')[0]
        shop = info.xpath('div[2]/div[3]/div[@class="shop"]/a/span[2]/text()')[0]
        city = info.xpath('div[2]/div[3]/div[@class="location"]/text()')[0]
        # print(detail, price, sell, shop, city)
        # print('='*30)
        data = {
            'detail': detail,
            'price': price,
            'sell': sell,
            'shop': shop,
            'city': city
        }
        collection.insert(data)
    if page <= 50:
        next_page(driver.current_url, page)
    else:
        sys.exit()


def next_page(url, page):
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_xpath('.//a[@class="J_Ajax num icon-tag"]').click()
    time.sleep(3)
    get_data(driver.current_url, page)


if __name__ == '__main__':
    url = 'https://www.taobao.com'
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.get(url)
    driver.find_element_by_id('q').clear()
    driver.find_element_by_id('q').send_keys('台式电脑')
    driver.find_element_by_class_name('btn-search').click()
    # print(driver.page_source)
    # driver.current_url获取当前页面的url
    get_data(driver.current_url, 1)  # 1表示第一页
