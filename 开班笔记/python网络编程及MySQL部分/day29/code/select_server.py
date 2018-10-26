from socket import *
from select import *
import sys

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('127.0.0.1',9999))
s.listen(10)

#将我们关注的IO放入rlist
rlist = [s]
wlist = []
xlist = [s]

while True:
	#print('等待IO')
	#wlist中有内容会立即返回
	rs,ws,xs = select(rlist,wlist,xlist)
	for r in rs:
		#表示套接字准备就绪
		if r is s:
			connfd,addr = r.accept()
			print('Connect from',addr)
			#将新的套接字加入到关注列表
			rlist.append(connfd)
		else:
			try:
				data = r.recv(1024)
				if not data:
					rlist.remove(r)
					r.close()
				else:
					print(r.getpeername(),':',data.decode('gbk'))
					#发送消息可以放到wlist列表中
					#r.send('copyright'.encode('gbk'))
					wlist.append(r)
			except Exception:
				pass
	
	for w in ws:
		w.send('牛逼的一匹'.encode('gbk'))
		wlist.remove(w)
	
	for x in xs:
		if x is s:
			s.close()
			sys.exit(1)