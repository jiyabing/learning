from socket import *
import os,sys,time

class Tftpclient(object):
	def __init__(self,sockfd):
		self.sockfd = sockfd
	
	def file_send(self,filename):
		with open(filename,'rb') as f:
			while True:
				data = f.read(64)
				if not data:
					time.sleep(0.5)
					self.sockfd.send(b'##')
					break
				self.sockfd.send(data)
	
	def do_list(self):
		self.sockfd.send(b'L')#发送请求类别
		#服务器回复Y/N
		data = self.sockfd.recv(1024).decode()
		if data == 'Y':
			data = self.sockfd.recv(4096).decode()
			files = data.split('#')
			for file in files:
				print(file)
			print('文件列表展示完毕')
		else:
			print('请求文件列表失败')
	
	def do_get(self,filename):
		self.sockfd.send(b'G' + filename.encode())
		data = self.sockfd.recv(2).decode()
		if data == 'OK':
			f = open(filename,'wb')
			print('下载中...')
			while True:
				data = self.sockfd.recv(64)
				if data == b'##':
					break
				f.write(data)
			f.close()
			print('%s下载完成！'%filename)
		else:
			print('文件不存在')

	def do_put(self,filename):
		self.sockfd.send(b'P' + filename.encode())
		data = self.sockfd.recv(8).decode()
		if data == 'e':
			s = input('文件已存在，是否继续？（y/n）')
			self.sockfd.send(s.encode())
			if s == 'y':
				self.file_send(filename)
				print('上传成功')		
		elif data == 'OK':
			self.file_send(filename)
			print('上传成功')

	def do_quit(self):
		self.sockfd.send(b'Q')
		self.sockfd.close()
		sys.exit(0)


def main():
	if len(sys.argv) < 3:
		print('argv is error')
		sys.exit(1)
	host = sys.argv[1]
	port = int(sys.argv[2])
	ADDR = (host,port)
	buffersize = 1024
	
	sockfd = socket()
	while True:
		try:
			sockfd.connect(ADDR)
			break
		except:
			print('正在尝试连接...')
			time.sleep(3)
			continue
	
	#创建客户端请求对象
	tftp = Tftpclient(sockfd)
	
	while True:
		print('=========MENU========')
		print('*********list********')
		print('*******get file******')
		print('*******put file******')
		print('*********quit********')
		print('=====================')
		data = input('输入命令>>')
		if data.strip() == 'list':
			tftp.do_list()
		elif data.strip()[:3] == 'get':
			if len(data.strip()) > 4:
				filename = data.strip()[4:]
				tftp.do_get(filename)
			else:
				print('请输入文件名')
		elif data.strip()[:3] == 'put':
			if len(data.strip()) > 4:
				filename = data.strip()[4:]
				tftp.do_put(filename)
			else:
				print('请输入文件名')
		elif data.strip() == 'quit':
			tftp.do_quit()
		else:
			print('请输入正确的命令！！！')
		



if __name__ == '__main__':
	main()
