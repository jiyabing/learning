"""
    这是一个用来测试的包

    此包有两个函数：
    以下省略...
"""
__all__ = ['menu','games'] #此类表只适用于from package import *

print('package包内的__init__.py被导入')

def fx():
    print('我是package包内的fx()函数')

fx()

name1= '我是package包内的name1变量'

import math #导入其他的包
print('package包被加载！',math.factorial(5))
