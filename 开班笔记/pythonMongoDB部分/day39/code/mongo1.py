#coding:utf8

#索引和聚合操作

from pymongo import MongoClient,IndexModel

conn = MongoClient('localhost',27017)
db = conn.stu
my_set = db.class4

#创建索引,并且将索引名返回
#index = my_set.ensure_index('name')
#print(index)

#复合索引
#index = my_set.ensure_index([('name',1),('king',-1)])
#print(index)

#唯一索引和稀疏索引
cls = db.class0
#唯一索引
#index = cls.ensure_index('name',unique=True)
#稀疏索引
#index = my_set.ensure_index('king_name',sparse=True)


#删除索引
#my_set.drop_index('name_1')
#my_set.drop_indexes()   #删除所有索引


#同时创建多个索引
#index1 = IndexModel([('name',1),('king',-1)])
#index2 = IndexModel([('king_name',1)])
#indexes = my_set.create_indexes([index1,index2])

#查看一个集合中的索引
#for i in my_set.list_indexes():
#	print(i)


#聚合管道
l = [{'$group':{'_id':'$king','count':{'$sum':1}}},{'$match':{'count':{'$gt':1}}}]
cursor = my_set.aggregate(l)
for i in cursor:
	print(i)

