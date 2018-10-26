from threading import Thread
from time import sleep

def music():
	while True:
		print('play music')
		sleep(2)
	
#创建线程和函数music关联	
t = Thread(target=music)

#启动线称
t.start()

#while True:
	#print('good good study')
	#sleep(1)
	
t.join()
print('========')

