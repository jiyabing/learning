#coding:utf8
'''
功能：完成httpserver部分
'''

from socket import *
import sys
import re 
from threading import Thread
#from WebFramework import app



#处理htttp请求
class HttpServer(object):
	def __init__(self,app):
		self.sockfd = socket()
		self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		self.app = app
	
	def bind(self,addr):
		self.sockfd.bind(addr)
	
	def start(self):
		self.sockfd.listen(10)
		while True:
			c, addr = self.sockfd.accept()
			print(addr,'用户连接')
			handle_thread = Thread(target=self.handle_client, args=(c,))
			handle_thread.start()
	
	def handle_client(self,c):
		#接受浏览器request
		request_data = c.recv(2048)
		request_lines = request_data.splitlines()
		#请求行
		request_line = request_lines[0].decode('utf-8')
		print(request_line)
		#get or post
		method = re.match(r'(\w+)\s+/\S*',request_line).group(1)
		filename = re.match(r'\w+\s+(/\S*)',request_line).group(1)
		print(method)
		print(filename)
		#要传递的内容打包成字典，传递给应用程序
		env = {'METHON':method,'PATH_INFO':filename}
		response_body = self.app(env, self.set_headers)
		print('============')
		response = self.response_headers + '\r\n' + response_body
		#向客户端发送response
		c.send(response.encode('utf8'))
		c.close()
	
	def set_headers(self,status,headers):
		'''
		在app调用该函数时，希望得到
		status = '200 OK'
		headers = [('Content-Type','text/plain')]
		'''
		response_headers = 'HTTP/1.1 ' + status + '\r\n'
		for header in headers:
			response_headers += '%s: %s\r\n'%header
		self.response_headers = response_headers

#完成httpserver对象属性的添加和创建
def main():
	#选择一个要使用的网站的某个app
	if len(sys.argv) < 2:
		sys.exit('''run the server as:
		python3 HttpServer.py FrameworkName:app''')
	#获取到这个网站下
	module_name, app_name = sys.argv[1].split(':')
	sys.path.insert(1,'.')
	m = __import__(module_name)
	app = getattr(m, app_name)
	
	#将该应用变为server对象的属性
	http_server = HttpServer(app)
	http_server.bind(('127.0.0.1',9999))
	print('Listen on port 9999')
	http_server.start()

if __name__ == '__main__':
	main()