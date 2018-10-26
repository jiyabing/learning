from tkinter import *
import time

def tick():
    global time1
    # 获取当前的系统时间
    time2 = time.strftime('%H:%M:%S')
    # 如果时间发生变化，代码自动更新显示的系统时间
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)
    clock.after(500, tick)
 
 
def show(frame):
    global time1,clock
    time1 = ''
    clock = Label(frame, font=('times', 34, 'bold'), bg='white')
    return clock