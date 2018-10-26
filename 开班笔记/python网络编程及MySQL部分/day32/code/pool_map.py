from multiprocessing import Pool
import time

def fun(fn):
	time.sleep(1)
	return fn * fn

test = [1,2,3,4]

if __name__ == '__main__':
	pool = Pool(processes = 4)
	r = pool.map(fun,test)
	print(r)
	pool.close()
	pool.join()