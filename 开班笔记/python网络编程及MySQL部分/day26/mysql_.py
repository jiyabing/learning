import pymysql
#1.创建数据库连接
db = pymysql.connect('localhost','root','123456','indexdb',
charset='utf8')

#2.创建游标对象
cursor = db.cursor()

#使用游标对象的方法操作数据库
cursor.execute('insert into new values(4,"sun");')
cursor.execute('delete from new where name="li";')


#提交commit
db.commit()

#关闭游标对象
cursor.close()

#关闭数据库连接
db.close()
