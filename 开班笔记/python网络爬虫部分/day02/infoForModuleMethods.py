# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 10:35:55 2018

@author: jyb
"""
# 0和1相当于一个开关,为0时打开b开关，为1时打开a开关
#print(0 and 'a' or 'b')
# 'b'
#print(1 and 'a' or 'b')
# 'a'


import requests

def printInfo(s, collapse=0):
    processFun = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    return processFun(s)

def info(object, spacing=15, collapse=0):
    '''
    遍历一遍object对象，把里面可以被调用的方法及方法的doc string打印出来
    '''
    # 1.提取出当前object可以被调用的方法列表
    methodList = [method for method in dir(object) if callable(
            getattr(object, method))]
#    print(methodList)
    
    # 2.需要把doc string的方法按照一定的格式提取出来
    processFun = collapse and (lambda s:" ".join(s.split())) or (lambda s:s)
    
    # 3.打印出方法的名称及其文档的说明
    print('\n'.join([
            "%s %s"%(method.ljust(spacing),
                     processFun(str(getattr(object, method).__doc__))) 
            for method in methodList]))
    

info(requests, collapse=1)
#s = 'str'
#info(s, collapse=1)
#print(printInfo(''.ljust.__doc__))

