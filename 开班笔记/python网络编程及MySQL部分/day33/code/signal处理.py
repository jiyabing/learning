import signal
from time import sleep


signal.alarm(5)

#采用默认的方法处理SIGALRM信号
signal.signal(signal.SIGALRM,signal.SIG_DFL)


#采用忽略信号处理方式
#signal.signal(signal.SIGALRM,signal.SIG_IGN)

while True:
	sleep(2)
	print('等待时钟....')