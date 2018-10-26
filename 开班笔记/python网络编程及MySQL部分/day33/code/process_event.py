from multiprocessing import Event,Process
from time import sleep

def wait_event():
	print('Process1也想操作临界区，但是要阻塞等待主进程')
	e.wait()
	print('主进程操作完了，轮到我了',e.is_set())

def wait_event_timeout():
	print('Process2也想操作临界区，但是要阻塞等待主进程')
	#设置等待超时为2秒
	e.wait(2)
	print('我等不了，还是去执行别的吧',e.is_set())

e = Event()

p1 = Process(name='block', target=wait_event)
p2 = Process(name='non-block', target=wait_event_timeout)

p1.start()
p2.start()

print('主进程正在忙碌的操作临界资源')
sleep(3)
e.set()
print('临界区以开放')

p1.join()
p2.join()
