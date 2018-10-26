from socket import *

sockfd = socket(AF_INET,SOCK_STREAM,0)


sockfd.connect(('127.0.0.1',9999))
print('连接成功')
#data = sockfd.recv(1024)
f = open('abc.bak.txt','w')

while True:
	data = sockfd.recv(1024).decode('gbk')
	if data == '##':
		break
	f.write(data)

f.close()
sockfd.close()
