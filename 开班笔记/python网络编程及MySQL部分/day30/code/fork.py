# coding:gbk
#os为系统相关模块，不同操作系统使用情况不同

import os
print('准备创建进程')
a = 1 #运行此程序后,子进程中也会有变量a

pid = os.fork()

if pid < 0:
    print('创建进程失败')
elif pid == 0:
    print('创建了一个新的进程a=',a)
else:
    print('这是原有的进程')

