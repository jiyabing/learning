from socket import *
import os,sys
import signal
import time

#文件库位置
file_path = '/home/jyb/'

class Tftpserver():
	def __init__(self,connfd):
		self.connfd = connfd
	
	def do_list(self):
		filelist = os.listdir(file_path)
		if not filelist:
			self.connfd.send(b'N')
			return
		else:
			self.connfd.send(b'Y')
		time.sleep(0.1)
		files = ''
		for filename in filelist:
			if filename[0] != '.' and os.path.isfile(file_path + filename):
				files += (filename + '#')
		self.connfd.send(files.encode())
	
	def do_get(self,filename):
		filelist = os.listdir(file_path)
		if filename not in filelist or (not os.path.isfile(file_path + filename)):
			self.connfd.send(b'N')
			return
		else:
			self.connfd.send(b'OK')
		time.sleep(0.1)
		f = open(file_path + filename,'rb')
		while True:
			data = f.read(64)
			if not data:
				time.sleep(0.5)
				self.connfd.send(b'##')
				break
			self.connfd.send(data)
		f.close()
	
	def do_put(self,filename):
		filelist = os.listdir(file_path)
		if filename in filelist and os.path.isfile(file_path + filename):
			self.connfd.send(b'e')
			data = self.connfd.recv(2).decode()
			if data == 'y':
				with open(file_path + filename + '.bak','wb') as f:
					while True:
						data = self.connfd.recv(64)
						#print(data)
						if data == b'##':
							break
						f.write(data)			
		else:
			self.connfd.send(b'OK')
			with open(file_path + filename,'wb') as f:
				while True:
					data = self.connfd.recv(64)
					if data == b'##':
						break
					f.write(data)
					
						
		
	
	#def do_quit(self):
		#pass
	

def main():
	if len(sys.argv) < 3:
		print('argv is error')
		sys.exit(1)
	host = sys.argv[1]
	port = int(sys.argv[2])
	ADDR = (host,port)
	buffersize = 1024
	
	sockfd = socket()
	sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
	sockfd.bind(ADDR)
	sockfd.listen(5)
	#处理僵尸进程
	signal.signal(signal.SIGCHLD,signal.SIG_IGN)

	while True:
		try:
			connfd,addr = sockfd.accept()
		except KeyboardInterrupt:
			sockfd.close()
			sys.exit(0)
		except Exception:
			continue
		print(addr,'客户登录')
		pid = os.fork()
		if pid < 0:
			print('创建子进程失败')
			connfd.close()
			continue
		elif pid == 0:
			sockfd.close()
			#创建客户端通信对象
			tftp = Tftpserver(connfd)
			while True:
				data = connfd.recv(buffersize).decode()
				if data[0] == 'L':
					tftp.do_list()
				elif data[0] == 'G':
					tftp.do_get(data[1:])
				elif data[0] == 'P':
					tftp.do_put(data[1:])
				elif data[0] == 'Q':
					print(addr,'客户退出')
					sys.exit(0)
		else:
			connfd.close()
			continue
			
if __name__ == '__main__':
	main()
