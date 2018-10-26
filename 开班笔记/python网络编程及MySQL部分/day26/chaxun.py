import pymysql

db = pymysql.connect('localhost','root','123456','indexdb',charset='utf8')

cursor = db.cursor()

sql_select = 'select * from new;'
cursor.execute(sql_select)

data = cursor.fetchone()
data2 = cursor.fetchmany(3)
print('结果为：',data)
print('结果为:',data2)

db.commit()
cursor.close()
db.close()


