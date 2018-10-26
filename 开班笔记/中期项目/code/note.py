from tkinter.filedialog import *
from tkinter.messagebox import *
import os

class mynote:
    def __init__(s):
        s.note_window()
        s.filename = ""
        s.mytextPad()
        s.mymenu()

    def note_window(s): # 便签主窗口
        s.top=Tk()
        s.top.title("便签")
        s.top.geometry("350x300+%d+350"%(s.top.winfo_screenwidth(
        ) - 360))

    def mynew(s): # 新建
        s.top.title("未命名文件")
        s.filename=None
        s.textPad.delete(1.0,END)

    def myopen(s): # 打开文件命令
        s.filename=askopenfilename(defaultextension=".txt")
        if s.filename=="":
            s.filename=None
        else:
            s.top.title("便签"+os.path.basename(s.filename))
            s.textPad.delete(1.0,END)
            f=open(s.filename,'r')
            s.textPad.insert(1.0,f.read())
            f.close()

    def mysave(s): # 保存命令
        try:
            f=open(s.filename,'w')
            msg=s.textPad.get(1.0,'end')
            f.write(msg)
            f.close()
        except:
            s.mysaveas()

    def mysaveas(s): # 另存为命令
        f=asksaveasfilename(initialfile="未命名.txt",defaultextension=".txt")
        s.filename=f
        fh=open(f,'w')
        msg=s.textPad.get(1.0,END)
        fh.write(msg)
        fh.close()
        s.top.title("便签"+os.path.basename(f))

    def mypopup(self,event): # 定义鼠标中键命令
        global editmenu
        editmenu.tk_popup(event.x_root,event.y_root)

    def search(self,needle,cssnstv,textPad,t,e):
        textPad.tag_remove("match","1.0",END)
        count=0
        if needle:
            pos="1.0"
            while True:
                pos=textPad.search(needle,pos,nocase=cssnstv,stopindex=END)
                if not pos:break
                lastpos=pos+str(len(needle))
                textPad.tag_add("match",pos,lastpos)
                count+=1
                pos=lastpos
            textPad.tag_config('match',fg='yellow',bg="green")
            e.focus_set()
            t.title(str(count)+"个被匹配")

    def mymenu(s):  # 菜单
        menubar=Menu(s.top)
        filemenu=Menu(s.top)
        filemenu.add_command(label="新建",command=s.mynew)
        filemenu.add_command(label="打开",command=s.myopen)
        filemenu.add_command(label="保存",command=s.mysave)
        filemenu.add_command(label="另存为",command=s.mysaveas)
        menubar.add_cascade(label="文件",menu=filemenu)
        s.top['menu']=menubar
    def mytextPad(s): # 定义顶条 侧边条 滚动条等
        shortcutbar=Frame(s.top,height=25,bg='light sea green')
        shortcutbar.pack(expand=NO,fill=X)
        Inlabe=Label(s.top,width=2,bg='antique white')
        Inlabe.pack(side=LEFT,anchor='nw',fill=Y)
        s.textPad=Text(s.top,undo=True)
        s.textPad.pack(expand=YES,fill=BOTH)
        scroll=Scrollbar(s.textPad)
        s.textPad.config(yscrollcommand=scroll.set)
        scroll.config(command=s.textPad.yview)
        scroll.pack(side=RIGHT,fill=Y)
        s.textPad.bind("<Button-3>",s.mypopup)

    def note_show(s):
        s.top.mainloop()


def run_note():
    note=mynote()
    note.note_show()
