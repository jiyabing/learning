from pymysql import *

class mysqlpython:
    def __init__(self,host,user,passwd,db,charset='utf8'):
        self.host = host
        #self.port =port
        self.db = db
        self.user = user
        self.passwd = passwd
        self.charset = charset
    
    def open(self):
        self.conn = connect(host=self.host,user=self.user,passwd=self.passwd,db=self.db,charset=self.charset)
        self.cursor = self.conn.cursor()
        print('游标对象已创建')
        
    def close(self):
        self.cursor.close()
        self.conn.close()
    
    def zhixing(self,sql):
        self.open()
        self.cursor.execute(sql)
        self.conn.commit()
        self.close()
        print('ok')

sqlh = mysqlpython('localhost','root','123456','indexdb')
sql_update = 'update new set id=10 where name="zhang";'
sqlh.zhixing(sql_update)




