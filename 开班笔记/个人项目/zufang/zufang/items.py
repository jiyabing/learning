# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZufangItem(scrapy.Item):
    # 定义要爬取的数据字段
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    # 出租类型(整租，主卧，次卧)
    lease_type = scrapy.Field()
    address = scrapy.Field()
    price = scrapy.Field()
