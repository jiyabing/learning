from socket import *

s = socket()
s.connect(('127.0.0.1',9999))

while True:
	msg = input('输入内容>>')
	s.send(msg.encode('gbk'))
	if not msg:
		break
	data = s.recv(1024)
	print(data.decode('gbk'))

s.close()