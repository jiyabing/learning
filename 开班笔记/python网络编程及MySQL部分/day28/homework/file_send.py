from socket import *
from time import sleep

sockfd = socket(AF_INET,SOCK_STREAM,0)

host = '127.0.0.1'
port = 9999
addr = (host,port)

sockfd.bind(addr)
sockfd.listen(5)

conn,addr = sockfd.accept()
print(addr,'已连接')

f = open('abc.txt','rb')
#conn.send('abc.txt'.encode('utf-8'))
while True:
	s = f.read(128)
	if not s:
		sleep(0.5)
		conn.send(b'##')
		break
	conn.send(s)
print('传输成功')

f.close()
conn.close()
sockfd.close()
