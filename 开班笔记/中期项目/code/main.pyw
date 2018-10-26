from tkinter import *
import web_search
import note
import filemanage
import tkinter_time
import date_time
import news
import weatherInfo

class Application:
    def __init__(self):
        self.width = 350
        self.height = 350
        self.create_mainWindow()
        self.maincolor()
        self.newsText()
        self.escButton()
        self.noteButton()
        self.fileButton()
        self.dateButton()
        self.weatherLabel()

    def create_mainWindow(self):  # 主窗口创建
        self.mainwindow = Tk()
        self.mainwindow.title('')
        self.mainwindow.overrideredirect(True)  # 隐藏边框
        self.mainwindow.attributes("-alpha", 0.85)  # 设置透明
        # 设置窗口默认位置
        start_position = [(self.mainwindow.winfo_screenwidth(
        ) - self.width), (self.mainwindow.winfo_screenheight())]
        self.mainwindow.geometry('%dx%d+%d+0' %
                                 (self.width, self.height, start_position[0]))

    def maincolor(self):  # 框架覆盖实现背景色
        frame = Frame(height=self.height, width=self.width, bg='white')
        self.frame = frame

    def escButton(self):  # 退出按钮
        esc_b = Button(self.frame, command=self.mainwindow.quit, text='退出')
        esc_b.place(relx=1, rely=0,anchor='ne',x=-5,y=5)  # 退出按钮的位置

    def newsText(self): # 新闻Text控件
        news_t=news.News_text(self.frame).news_l
        news_t.place(x=2,y=2)

    def noteButton(self): # 便签按钮
        note_b = Button(self.frame, command=note.run_note, text='便签')
        note_b.place(relx=0,rely=1,anchor='sw',x=105,y=-25)

    def fileButton(self): # 整理桌面
        file_b = Button(self.frame, command=filemanage.do_file, text='整理桌面')
        file_b.place(relx=0,rely=1,anchor='sw',x=30,y=-25)

    def dateButton(self): #日期显示
        var = StringVar()
        var.set(date_time.now_date()+'\n\n'+date_time.get_weekday())
        date_b = Button(self.frame, command=date_time.func,
                        textvariable=var, relief=FLAT,bg='white',
                        justify=CENTER, font=('', 14,))
        date_b.place(relx = 0.7,rely = 0.45,anchor = CENTER,y=50)

    def weatherLabel(self): # 天气Label控件
        w=weatherInfo.weather(self.frame)
        w.l.place(relx=0,rely=0.8,x=20,y=-12)
        w.img_info.place(relx=0,rely=0.3,x=35,y=15)
        w.w_info.place(relx=0,rely=0.5,x=20,y=15)
        w.w_city.place(relx=0,rely=0.3,x=10,y=-20)
        w.cbox.place(relx=0,rely=0.3,x=45,y=-20)


    def show(self):  # 显示窗口
        web_search.search_entry(self.frame).place(relx=0.5, rely=1,anchor='s',x=30,y=-30)  # 搜索模块的搜索框位置
        web_search.search_button(self.frame).place(relx=0.7, rely=1,anchor='s',x=70,y=-25)  # 搜索模块的搜索按钮位置
        tkinter_time.show(self.frame).place(relx = 0.7,rely = 0.45,anchor=CENTER, y=-30) # 时间显示
        tkinter_time.tick() # 时间刷新
        self.frame.pack(expand=YES, fill=BOTH)
        self.mainwindow.mainloop()  # 主窗口循环


if __name__ == '__main__':
    main = Application()
    main.show()
