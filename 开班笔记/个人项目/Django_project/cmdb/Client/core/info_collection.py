#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 该模块的作用很简单：
#     1.首先通过Python内置的platform模块获取执行main脚本的操作系统类别，通常是windows和Linux；
#     2.根据操作系统的不同，反射获取相应的信息收集方法，并执行
#     3.如果是客户端不支持的操作系统，比如苹果系统，则提示并退出客户端。


import sys
import platform


def linux_sys_info():
    from plugins.linux import sys_info
    return sys_info.collect()


def windows_sys_info():
    from plugins.windows import sys_info as win_sys_info
    return win_sys_info.collect()


class InfoCollection(object):
    def collect(self):
        # 收集平台信息
        # 首先判断当前平台，根据平台的不同，执行不同的方法
        try:
            func = getattr(self, platform.system())
            info_data = func()
            formatted_data = self.build_report_data(info_data)
            return formatted_data
        except AttributeError:
            sys.exit("不支持当前操作系统： [%s]! " % platform.system())

    def Linux(self):
        return linux_sys_info()

    def Windows(self):
        return windows_sys_info()

    def build_report_data(self, data):
        # 留下一个接口，方便以后增加功能或者过滤数据
        return data
