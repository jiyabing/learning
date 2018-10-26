import time

def app(environ,start_response):
	status = '200 Ok'
	response_headers = [('Content-Type','text/plain;charset=UTF-8')]
	
	start_response(status,response_headers)
	
	return '\n=====简单的app程序=======\n%s'%time.ctime()
