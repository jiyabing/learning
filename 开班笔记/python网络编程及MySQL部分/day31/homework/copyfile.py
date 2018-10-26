import multiprocessing as mp
import sys,os

#获取文件大小
#size = os.path.getsize('abc.txt')

f = open('abc.txt','rb')
bs = f.read()
f.close()
bs1 = bs[:len(bs)//2]
bs2 = bs[len(bs)//2:]
#print(bs1)
#print(bs2)

def cpfile1():
	f = open('new1.txt','wb')
	f.write(bs1)
	f.close()

def cpfile2():
	f = open('new2.txt','wb')
	f.write(bs2)
	f.close()



p1 = mp.Process(target=cpfile1)
p2 = mp.Process(target=cpfile2)

if __name__ == '__main__':
	p1.start()
	p2.start()
	
	p1.join()
	p2.join()