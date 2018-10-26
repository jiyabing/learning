#多进程tcp

from socketserver import *

class Server(ForkingMixIn,TCPServer):
	pass

#处理具体请求
class Handler(StreamRequestHandler):
	def handle(self):
		#self.request 相当于accept创建的新的套接字
		addr = self.request.getpeername()
		print('Connect from',addr)
		while True:
			data = self.request.recv(1024).decode()
			print(data)
			if not data:
				break
			self.request.send('收到'.encode())
	
server = Server(('127.0.0.1',9999),Handler)
server.serve_forever()


