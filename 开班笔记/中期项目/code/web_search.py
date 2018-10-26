import webbrowser
from tkinter import *

def search_entry(frame):    # 搜索框
    global e
    e = Entry(frame,bg='#FFFFCC',width=15)
    e.bind('<Key-Return>',search_command) # 将回车键绑定至搜索
    return e

def search_command(key=None):   # 实现搜索功能
    msg = e.get()
    if msg:
        webbrowser.open("https://www.baidu.com/s?ie=utf-8&wd=%s" % msg)


def search_button(frame): # 创建搜索按钮
    com = Button(frame,text = '网络搜索', command = search_command)
    return com



