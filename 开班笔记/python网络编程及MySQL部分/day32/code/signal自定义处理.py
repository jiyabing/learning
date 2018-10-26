from signal import *
import time


def func(sig,frame):
	if sig == SIGALRM:
		print(sig)#打印信号标识
		print('收到时钟信号')
	elif sig == SIGINT:
		print('就不结束')
	

alarm(7)

#通过自定义方法处理
signal(SIGALRM,handler)
signal(SIGINT,handler)

while True:
	print('等待信号处理...')
	time.sleep(2)