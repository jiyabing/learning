# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 14:52:45 2018

@author: jyb
"""

def fab3(n):
    index, a, b, = 0, 0, 1
    while index < n:
        yield b #保留当前的函数的上下文，进入阻塞等待状态
        a, b = b, a+b
        index += 1

if __name__ == '__main__':
    f = fab3(7)
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))
    print(next(f))

