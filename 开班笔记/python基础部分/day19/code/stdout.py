#stdout.py
#此程序示意标准输出sys.stdout和标准错误输出sys.stderr
import sys

sys.stdout.write('hello world\n')
#等同于print('hello world',end='\n')



#以下程序会出错
#sys.stdout.close()
#print('程序结束')


#标准错误输出
sys.stderr.write('我的出现是个错误！\n')
