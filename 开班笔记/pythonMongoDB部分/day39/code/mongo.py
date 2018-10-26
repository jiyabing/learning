#coding:utf8
#通过pymongo进行增删改查
from pymongo import MongoClient

#创建连接对象
conn = MongoClient('localhost',27017)

#创建集合对象和数据库对象
#方法一
# db = conn.stu
# my_set = db.class4

#方法二
db = conn['stu']
print(db)
print(type(db))
my_set = db['class4']

#print(my_set)
#print(dir(my_set))

#插入数据
#my_set.insert({'name':'张','king':'乾隆'})
# my_set.insert([{'name':'陈道明','king':'康熙'},{'name':'张国立','king':'康熙'}])
# my_set.insert_many([{'name':'唐国强','king':'雍正'},{'name':'陈建斌','king':'雍正'}])
# my_set.insert_one({'name':'郑少秋','king':'乾隆'})
# my_set.save({'name':'吴奇隆','king':'四爷'})

#删除数据
#my_set.remove({'name':'吴奇隆'})

#只删除第一条符合条件的文档
#my_set.remove({'name':'陈道明'},multi = False)

#删除所有文档
#my_set.remove()


#查找操作
cursor = my_set.find({},{'_id':0})
# for i in cursor:
#     print(i['name'],'-----',i['king'])

#print(cursor.next())
print(cursor.count())
# for i in cursor.skip(2).limit(3):
#     print(i)

# for i in cursor.sort([('name',-1)]):
#     print(i)

#更换集合
# my_set1 = db.class1
# for i in my_set1.find({'age':{'$lt':20}},{'_id':0}):
#     print(i)

# for i in my_set1.find({'hobby':{'$size':3}},{'_id':0}):
#     print(i)


#数据修改
#my_set.update({'name':'张国立'},{'$set':{'name':'国立'}})

#文档不存在则插入文档
# my_set.update({'name':'贾静雯'},
#     {'$set':{'king':'武则天'}},upsert = True)

#修改多条文档
# my_set.update({'king':'康熙'},
#     {'$set':{'king_name':'玄烨'}},multi = True)

# my_set.update_many({'king':'雍正'},
#     {'$set':{'king_name':'胤禛'}})

# my_set.update_one({'king_name':None},
#     {'$set':{'king_name':'弘历'}})

#my_set.update({'name':'贾静雯'},{'$unset':{'king_name':0}})

#查找并删除，查找结果会返回
#print(my_set.find_one_and_delete({'name':'贾静雯'}))

conn.close()
