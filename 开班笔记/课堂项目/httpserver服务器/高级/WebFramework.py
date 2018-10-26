#coding:utf8

'''
功能：完成后端请求处理服务代码
说明：模拟web框架的基本原理
'''
import time
#设置静态网页文件夹
html_root_dir = './static'

#Python方法
PYTHON_DIR = './wsgiPy'

class Application():
	def __init__(self,urls):
		self.urls = urls
	
	def __call__(self, env, set_headers):
		path = env.get('PATH_INFO', '/')
		#/static/index.html 表示要获取静态文件
		#/time 表示用Python方法处理请求
		if path.startswith('/static'):
			file_name = path[7:]
			print('66666666',file_name)
			try:
				f = open(html_root_dir + file_name, 'rb')
			except IOError:
				#代表没有找到该静态网页
				status = '404 Not Found'
				headers = []
				set_headers(status,headers)
				return '<h1>==sorry not found the page==<h1>'
			else:
				file_data = f.read()
				f.close()
				
				status = '200 OK'
				headers = []
				set_headers(status,headers)
				return file_data.decode('utf8')
		else:
			for url,handler in self.urls:
				if path == url:
					return handler(env,set_headers)
			#请求的url未找到
			status = '404 Not Found'
			headers = []
			set_headers(status,headers)
			return 'sorry url not Found'

def show_time(env,set_headers):
	status = '200 Ok'
	headers = []
	set_headers(status,headers)
	return time.ctime()

def say_hello(env,set_headers):
	status = '200 Ok'
	headers = []
	set_headers(status,headers)
	return 'say hello'

def say_bye(env,set_headers):
	status = '200 Ok'
	headers = []
	set_headers(status,headers)
	return 'say bye'
	
urls = [('/time',show_time),('/hello',say_hello),('/bye',say_bye)
]

app = Application(urls)