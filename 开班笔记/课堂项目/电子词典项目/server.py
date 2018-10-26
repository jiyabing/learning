#coding:utf-8

'''
name:jyb
date:2018-5-30
This is a dict project for AID 1803
'''

from socket import *
import os
import signal
import time
import pymysql
import sys

dict_text = './dict.txt' #字典路径
host = '127.0.0.1'
port = 9999
ADDR = (host,port)


#主流程控制
def main():
	db = pymysql.connect('localhost','root','123456','dictdb')
	
	s = socket()
	s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	s.bind(ADDR)
	s.listen(5)
	#忽略子进程退出
	signal.signal(signal.SIGCHLD,signal.SIG_IGN)
	
	while True:
		try:
			c,addr = s.accept()
			print('Connect from',addr)
		except KeyboardInterrupt:
			sys.exit(0)
		except:
			continue
		
		#创建子进程
		pid = os.fork()
		if pid < 0:
			print('子进程创建失败')
			c.close()
		elif pid == 0:
			s.close()
			do_child(c,db,addr)
		else:
			c.close()
			continue
	

def do_child(c,db,addr):
	#循环接受请求
	while True:
		data = c.recv(128).decode()
		print('Request:',data)
		if not data:
			print(addr,'客户端意外断开')
			break
		elif data[0] == 'R':
			do_register(c,db,data)
		elif data[0] == 'L':
			do_login(c,db,data)
		elif data[0] == 'E':
			c.close()
			sys.exit(0)
		elif data[0] == 'Q':
			do_query(c,db,data)
		elif data[0] == 'H':
			do_history(c,db,data)


def do_register(c,db,data):
	print('执行注册操作')
	l = data.split(' ')
	name = l[1]
	passwd = l[2]
	
	cursor = db.cursor()
	sql = "select * from user where name='%s'"%name
	cursor.execute(sql)
	r = cursor.fetchone()
	if r != None:
		c.send(b'EXISTS')
		return
	sql = "insert into user(name,passwd) values('%s','%s')"%(name,passwd)
	try:
		cursor.execute(sql)
		db.commit()
		c.send(b'ok')
	except:
		c.send(b'fail')
		db.rollback()
		return
	else:
		print('注册成功')


def do_login(c,db,data):
	print('登录操作')
	l = data.split(' ')
	name = l[1]
	passwd = l[2]
	
	cursor = db.cursor()
	try:
		sql = "select * from user where name='%s' and passwd='%s'"%(name,passwd)
		cursor.execute(sql)
		r = cursor.fetchone()
	except:
		pass
	if r == None:
		c.send(b'fail')
	else:
		c.send(b'ok')


def do_query(c,db,data):
	print('查询操作')
	l = data.split(' ')
	name = l[1]
	word = l[2]
	cursor = db.cursor()
	
	def insert_history():
		tm = time.ctime()
		sql = 'insert into history(name,word,time) values("%s","%s","%s")'%(name,word,tm)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
			return
	
	#操作文本
	'''		
	try:
		f = open(dict_text,'rb')
		print('文件打开')
	except:
		c.send(b'fail')
		return
	while True:
		line = f.readline().decode()
		tmp = line.split(' ')
		if tmp[0] > word:
			c.send(b'fail')
			f.close()
			break
		if tmp[0] == word:
			c.send(b'ok')
			time.sleep(0.1)
			c.send(line.encode())
			insert_history()
			break
	f.close()
	'''
	
	#操作数据库
	try:
		sql = 'select * from words where word="%s"'%word
		cursor.execute(sql)
		r = cursor.fetchone()
	except:
		c.send(b'fail')
		return
	while True:
		if r == None:
			c.send(b'fail')
			break
		else:
			c.send(b'ok')
			time.sleep(0.1)
			c.send(r[2].encode())
			insert_history()
			break
			

def do_history(c,db,data):
	print('历史查询')
	name = data.split(' ')[1]
	cursor = db.cursor()
	try:
		sql = 'select * from history where name="%s"'%name
		cursor.execute(sql)
		r = cursor.fetchall()
		if not r:
			c.send(b'fail')
		else:
			c.send(b'ok')
	except:
		pass
	for i in r:
		time.sleep(0.1)
		msg = '%s %-20s %s'%(i[1],i[2],i[3])
		c.send(msg.encode())
	time.sleep(0.1)
	c.send(b'##')		

if __name__ == "__main__":
	main()
