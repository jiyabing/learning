# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class ZufangPipeline(object):
    # def spider_start(self, spider):
    #     self.con = sqlite3.connect('zufang.sqlite')
    #     self.cu = self.con.cursor()

    def process_item(self, item, spider):
        print(spider.name, 'pipelines')
        # sql = "insert into zufang (title, price) value ('{}', '{}')".format(item['title'], item['price'])
        # self.cu.execute(sql)
        # self.con.commit()
        with open('E:/学习文件/python学习资料/开班笔记/个人项目/zufang/zufang/zufang.text', 'a+') as fw:
            fw.write(item['title'] + '\n')
            fw.write(item['lease_type'] + '\n')
            fw.write(item['address'] + '\n')
            fw.write(item['price'] + '\n')
        return item

    # def spider_end(self, spider):
    #     self.con.close()
