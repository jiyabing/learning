from multiprocessing import Value,Process
import time
import random

def deposite(money):
	for i in range(100):
		time.sleep(0.03)
		money.value += random.randint(1,100)

		
def withdraw(money):
	for i in range(100):
		time.sleep(0.02)
		money.value -= random.randint(1,50)


#创建共享内存对象
money = Value('i',2000)

if __name__ == '__main__':
	d = Process(target = deposite,args = (money,))
	w = Process(target = withdraw,args = (money,))
	
	d.start()
	w.start()
	
	d.join()
	w.join()
	
	print(money.value)