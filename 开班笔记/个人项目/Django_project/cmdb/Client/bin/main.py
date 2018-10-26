#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
1.通过os和sys模块的配合，将当前客户端所在目录设置为工作目录，如果不这么做，会无法导入其它模块；
2.handler模块是核心代码模块，在core目录中
3.以后调用客户端就只需要执行 “python main.py 参数” 就可以了
"""
import os
import sys


BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)
from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
