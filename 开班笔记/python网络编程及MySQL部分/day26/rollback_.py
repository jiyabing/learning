import pymysql

db = pymysql.connect('localhost','root','123456','commit',charset='utf8')

cur = db.cursor()

try:
    cur.execute('update CCB set money=5000 where name="zhuanqian";')
    cur.execute('update ICBC ...;')
    db.commit()
    print('成功转账')
except Exception as e:
    db.rollback()
    print('出现错误，已回滚')

cur.close()
db.close()
