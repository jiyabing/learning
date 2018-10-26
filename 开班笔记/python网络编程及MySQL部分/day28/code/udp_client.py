from socket import *
import sys

#从命令行传入ip和端口
if len(sys.argv) < 3:
	print('argv is error!!!')

host = sys.argv[1]
port = int(sys.argv[2])
ADDR = (host,port)
buffersize = 1024

#1.创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM,0)

#2.收发消息
while True:
	data = input('输入消息，按回车退出>>')
	#按回车退出
	if not data:
		break
	#发消息
	sockfd.sendto(data.encode('gbk'),ADDR)
	
	#收消息
	data,addr = sockfd.recvfrom(buffersize)
	if not data:
		print('服务器已断开！')
		break
	print('从服务器收到：',data.decode('gbk'))

sockfd.close()