'''
完成httpserver的并发
并发使用多线程
用不同的后端程序处理不同的请求
可以简单的显示静态页面
'''

import sys
from socket import *
from threading import Thread

#全局变量
addr = ('',9999)

#存静态网页
static_root = './static'

#存放python处理模块
handler_root = './handler'

#httpserver类
class HttpServer(object):
	def __init__(self,addr):
		self.sockfd = socket()
		self.sockfd.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
		self.sockfd.bind(addr)
		self.sockfd.listen(5)
		self.serverName = '127.0.0.1'
		self.serverPort = 9999
	
	#服务器启动函数：接收客户端请求，创建新的线程
	def serverForever(self):
		while True:
			self.connfd,self.caddr = self.sockfd.accept()
			clientTread = Thread(target=self.handlerRequest)
			clientTread.start()
	
	def setApp(self,application):
		self.applicaton = application
	
	def handlerRequest(self):
		#接收request请求
		self.recvData = self.connfd.recv(2048)
		requestHeaders = self.recvData.splitlines()
		for line in requestHeaders:
			print(line)
		
		#获取到从浏览器输入的具体请求
		getRequest = str(requestHeaders[0]).split(' ')[1]
		if getRequest[-3:] != '.py':
			if getRequest == '/':
				getFilename = static_root + '/index.html'
			else:
				getFilename = static_root + getRequest
			
			try:
				f = open(getFilename)
			except:
				responseHeaders = 'HTTP/1.1 404 not found\r\n'
				responseHeaders += '\r\n'
				responseBody = '=====sorry,file not find======'
			else:
				responseHeaders = 'HTTP/1.1 200 OK\r\n'
				responseHeaders += '\r\n'
				responseBody = f.read()
			finally:
				response = responseHeaders + responseBody
				self.connfd.send(response.encode())
		else:
			#需要的环境变量
			env = {}
			bodyContent = self.application(env,self.startResponse)
			response = "HTTP/1.1 {status}\r\n".format(self.header_set[0])
			for header in self.header_set[1:]:
				response += '{0}:{1}\r\n'.format(*header)
			response += '\r\n'
			response += bodyContent
			
			self.connfd.send(response.encode())
		
		self.connfd.close()
			
	def startResponse(self,status,response_handers):
		serverHeaders = [('Data','2018/5/21'),('server','HTTPServer 1.0'),]
		self.header_set = [status,response_headers + serverHeaders]

#控制服务器启动
def main():
	#启动时直接告知使用哪个模块哪个函数处理请求
	#python3 new_httpServer.py module app
	if len(sys.argv) < 3:
		sys.exit('请选择一个模块和应用')
		
	#将handler文件夹加入搜索路径
	sys.path.insert(0,handler_root)
	#导入modul模块
	m = __import__(sys.argv[1])
	#获取module下的app,赋给一个变量
	application = getattr(m,sys.argv[2])
		
	httpd = HttpServer(addr)
	httpd.setApp(application)
	print('Serving HTTP on port 9999')
	httpd.serverForever()
	

if __name__ == '__main__':
	main()
