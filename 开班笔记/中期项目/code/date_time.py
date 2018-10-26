# coding:utf-8
from tkinter import *
import calendar
from datetime import date, datetime

m = datetime.now().month
y = datetime.now().year


def get_cal(year=datetime.now().year, month=datetime.now().month):
    return calendar.month(year, month)


def now_date():
    return '{}年{}月{}日'.format(datetime.now().year, datetime.now().month, datetime.now().day)


def get_weekday():
    dict = {0: '星期一', 1: '星期二', 2: '星期三', 3: '星期四', 4: '星期五', 5: '星期六', 6: '星期天'}
    n = calendar.weekday(datetime.now().year, datetime.now().month, datetime.now().day)
    s = dict.get(n)
    return s


def func():
    r = Tk()
    r.title('')
    w=r.winfo_screenwidth()-615
    r.geometry('+%d+0'%w)
    frm_l = Frame(r)
    t = Text(frm_l, width=20, height=7, font=('宋体', 14))
    t.insert(1.0, get_cal(datetime.now().year, datetime.now().month))
    t.pack()

    def caladd():
        global m, y
        m += 1
        if m > 12:
            y += 1
            m = 1
        t.delete(1.0, 10.0)
        t.insert(1.0, get_cal(y, m))

    def calsub():
        global m, y
        m -= 1
        if m < 1:
            y -= 1
            m = 12
        t.delete(1.0, 10.0)
        t.insert(1.0, get_cal(y, m))

    frm_r = Frame(r)
    Button(frm_r, text='<', command=calsub, width=2, height=1).pack(side=LEFT)
    Button(frm_r, text='>', command=caladd, width=2, height=1).pack(side=RIGHT)
    frm_l.pack(side=LEFT)
    frm_r.pack(side=RIGHT)
    r.mainloop()
# if __name__ == '__main__':
#     print(get_weekday())
