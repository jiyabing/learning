#coding:utf8

from pymongo import MongoClient
import bson.binary
import time

#连接mongo服务器
conn = MongoClient('localhost',27017)

#选择数据库,如没有则自动创建
db = conn.file

#选择集合,如没有自动创建
my_set = db.img

#将文件存储到数据库
#打开要存储的文件
'''
with open('/home/tarena/桌面/img.jpg','rb') as f:
	data = f.read()
	#将读取的二进制流转换成bson格式二进制的子串
	content = bson.binary.Binary(data)
	
	#将content内容插入到img集合中
	my_set.insert({'filename':'img.jpg','data':content,'date':time.ctime()})
'''
	
#从数据库中提取文件
#选择要提取的文件
data = my_set.find_one({'filename':'img.jpg'})
#print(data)


#获取文件内容
with open('/home/tarena/桌面/'+data['filename'],'wb') as f:
	f.write(data['data'])

conn.close()

	
