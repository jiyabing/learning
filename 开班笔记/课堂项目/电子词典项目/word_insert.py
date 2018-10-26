import pymysql
import re

db = pymysql.connect('localhost','root','123456','dictdb',charset='utf8')
cursor = db.cursor()


#cursor.execute('create table words(id int unsigned primary key auto_increment,word varchar(32) not null,jieshi varchar(500),index(word)) default charset=utf8;')


f = open('dict.txt','r')
while True:
	line = f.readline()
	if line:
		l = re.split(r'\s+',line)
		s1 = l[0]
		s2 = ' '.join(l[1:]).strip()
		#print(s2)
		try:
			sql = "insert into words(word,jieshi) values('%s','%s');"%(s1,s2)
			cursor.execute(sql)
		except:
			pass
	else:
		break

f.close()

db.commit()
cursor.close()
db.close()
