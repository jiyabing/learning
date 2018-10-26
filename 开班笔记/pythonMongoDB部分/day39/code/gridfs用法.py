#coding:utf-8
import pymongo
import gridfs
#print(dir(gridfs))

conn = pymongo.MongoClient('localhost',27017)
db = conn.my_env

#获取gridfs对象
fs = gridfs.GridFS(db)
#print(fs)

#得到gridfs对象中所有文件的游标
files = fs.find()
#print(type(files))
#print(files)
#print(files.count())

#
for file in files:
	
	#获取文件名
	#print(file.filename)
	
	if file.filename == 'abc.mp3':
		with open('/home/tarena/桌面/'+file.filename,'wb') as f:
			#通过file的read()函数读取文件内容
			data = file.read()
			if not data:
				break
			f.write(data)
			print('完成')

conn.close()


