# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class JianshuPipeline(object):
    def __init__(self):
        client = pymongo.MongoClient('127.0.0.1', 27017)
        db = client['js_db']
        collection = db['jianshu']
        self.post = collection

    def process_item(self, item, spider):
        info = dict(item)
        self.post.insert(info)
        return item
