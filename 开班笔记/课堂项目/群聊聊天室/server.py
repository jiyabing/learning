'''
name:Levi
chatroom server
'''
from socket import *
import os,sys

#实现登录
def do_login(s,user,name,addr):
	#判断用户名是否存在
	if (name in user) or name == '管理员':
		s.sendto('该用户名已存在,请重新输入'.encode(),addr)
		return
	s.sendto(b'OK',addr)
	msg = '\n欢迎%s进入聊天室' %name
	
	#通知所有人
	for i in user:
		s.sendto(msg.encode(),user[i])
		
	#将用户加入字典
	user[name] = addr
	return

def do_chat(s,user,cmd):
	msg = '\n%-4s:%s'%(cmd[1],' '.join(cmd[2:]))
	#发送给所有人除了自己
	for i in user:
		if i != cmd[1]:
			s.sendto(msg.encode(),user[i])
	return

def do_quit(s,user,name):
	del user[name]
	msg = '\n' + name + '离开了聊天室'
	for i in user:
		s.sendto(msg.encode(),user[i])
	return

#子进程处理客户端请求
def do_child(s):
	#print('这是子进程')
	#字典用来存储用户信息
	user = {}
	#循环接受请求
	while True:
		msg,addr = s.recvfrom(1024)
		msg = msg.decode()
		cmd = msg.split(' ')
		
		#根据不同请求作不同事情
		if cmd[0] == 'L':
			do_login(s,user,cmd[1],addr)
		
		elif cmd[0] == 'C':
			do_chat(s,user,cmd)
		
		elif cmd[0] == 'Q':
			do_quit(s,user,cmd[1])
			
		else:
			s.sendto('请求错误'.encode(),addr)
			


#发送管理员消息
def do_parent(s,addr):
	#print('这是父进程')
	while True:
		msg = input('输入广播内容：')
		msg = 'C 管理员 ' + msg
		s.sendto(msg.encode(),addr)
	s.close()
	sys.exit(0)


def main():
	if len(sys.argv) < 3:
		print('argv is error')
		return
	
	host = sys.argv[1]
	port = int(sys.argv[2])
	ADDR = (host,port)
	
	#使用数据报套接字
	s = socket(AF_INET,SOCK_DGRAM)
	s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	s.bind(ADDR)
	
	#创建一级子进程
	pid1 = os.fork()

	if pid1 < 0:
		print('创建一级子进程失败')

	elif pid1 == 0:
		pid2 = os.fork()
		if pid2 < 0:
			print('创建二级子进程失败')
		elif pid2 == 0:
			do_child(s)
		else:
			#一级子进程退出，使二级子进程成为孤儿
			os._exit(0)

	else:
		#等待一级子进程退出
		os.wait()
		do_parent(s,ADDR)

if __name__ == '__main__':
	main()
