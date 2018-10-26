# coding=utf-8
import json
import urllib.request
import time
from tkinter import ttk
from tkinter import *

# url = http://www.nmc.cn/f/rest/real/城市代码
# url = http://www.nmc.cn/f/rest/tempchart/城市代码
# fiddler抓包工具

# 模拟成浏览器
headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Encoding": "gbk,utf-8,gb2312",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": "Mozilla/5.0(Windows NT 10.0; WOW64) AppleWebKit/537.36(KHTML, like Gecko) \
           Chrome/55.0.2883.87 Safari/537.36",
           "Connection": "keep-alive"}
opener = urllib.request.build_opener()
headall = []
for key, value in headers.items():
    item = (key, value)
    headall.append(item)
opener.addheaders = headall
# 将opener安装为全局
urllib.request.install_opener(opener)

# 构造数据，城市分别是北京、天津、石家庄、太原、济南、沈阳、呼和浩特、郑州、武汉
city_id = {'北京': '54511', '天津': '54517', '石家庄': '53698', '济南': '54823',
           '沈阳': '54342', '呼和浩特': '53463', '武汉': '57494'}

weather_image = {'晴': '0.gif', '多云': '1.gif', '阴': '2.gif', '阵雨': '3.gif', '冻雨': '5.gif', '雨加雪': '6.gif', '中雨': '8.gif', '大雨': '9.gif', '暴雨': '10.gif','雷阵雨': '4.gif', '大暴雨': '11.gif', '特大暴雨': '12.gif', '小雪': '13.gif', '中雪': '14.gif', '大雪': '15.gif', '暴雪': '16.gif', '阵雪': '17.gif', '雾': '18.gif', '沙尘暴': '19.gif', '强沙尘暴': '20.gif', '小雨': '7.gif', '-': '7.gif'}


def get_weather(city='武汉'):
    while True:
        try:
            url = "http://www.nmc.cn/f/rest/real/" + city_id.get(city)
            stdout = urllib.request.urlopen(url)
            weather_info = stdout.read().decode('utf-8')
            json_data = json.loads(weather_info)
            return json_data
        except urllib.error.URLError:
            print("获取天气状况数据出现URLERROR！一分钟后重试……")
            time.sleep(60)
            # 出现异常则过一段时间重新执行此部分
            return 'URL错误'
        except Exception:
            print("获取天气状况数据出现EXCEPTION！十秒钟后重试……")
            time.sleep(10)
            # 出现异常则过一段时间重新执行此部分
            continue


def min_max_temp(city='武汉'):
    while True:
        try:
            url = 'http://www.nmc.cn/f/rest/tempchart/' + city_id.get(city)
            stdout = urllib.request.urlopen(url)
            temperature_info = stdout.read().decode('utf-8')
            json_data = json.loads(temperature_info)
            return json_data
        except:
            print('网络异常')
            time.sleep(5)
            continue


def get_image(city='武汉'):
    img = weather_image.get(get_weather(city)['weather']['info'])
    return img

def func1(event, city):
    l = min_max_temp(city)[8:11]
    r = Toplevel()
    r.geometry("+%d+0"%(r.winfo_screenwidth(
        ) - 750))
    for i in range(3):	
    	frm = Frame(r)
    	var = StringVar()
    	Lab = Label(frm, textvariable=var)
    	var.set(l[i]['realTime'][:4]+'-'+l[i]['realTime'][4:6]+'-'+l[i]['realTime'][6:])
    	Lab.pack()
    	p = PhotoImage(file='天气/' + l[i].get('dayImg') + '.gif')
    	L = Label(frm, image=p, bg='#D8E5F2')
    	L.p = p
    	L.pack()
    	Label(frm, text='温度：' + str(l[i].get('minTemp')) + '℃--' + str(l[i].get('maxTemp')) + '℃').pack()
    	frm.pack(side=LEFT)
    r.mainloop()

# 天气部分
class weather:
    def __init__(s,frame):
        s.frame=frame
        s.weather_c()
        s.weather_f()
        s.weather_p()
        s.weather_l()

    def weather_c(s):
        s.w_city=Label(s.frame, text='城市：',bg="white")
        cbox = ttk.Combobox(s.frame, values=list(city_id.keys()), state='readonly', width=8)
        cbox.current(6)
        cbox.bind('<<ComboboxSelected>>', lambda x: s.change_city(x, cbox.get()))
        # cbox.pack(side=RIGHT)
        s.cbox=cbox


    def weather_f(s):
        l = Label(s.frame, text='未来三天天气情况>>',bg='white')
        l.bind('<Button-1>', lambda x: func1(x, s.cbox.get()))
        # l.pack()
        s.l=l

    def weather_p(s):
        photo = PhotoImage(file='天气/' + get_image())
        s.photo=photo
        img_info = Label(s.frame, background='#D8E5F2', image=photo)
        # img_info.pack()
        s.img_info=img_info

    def weather_l(s):
        weather_dict = get_weather(s.cbox.get())
        var = StringVar()
        if weather_dict['wind']['direct'] == '9999':
            var.set(weather_dict['weather']['info']+'\n实时温度：'+str(weather_dict["weather"]["temperature"])+'℃\n'+'-- '+weather_dict['wind']['power']+'\n湿度：'+str(weather_dict['weather']['humidity'])+'%')
        else:
        	var.set(weather_dict['weather']['info']+'\n实时温度：'+str(weather_dict["weather"]["temperature"])+'℃\n'+ weather_dict['wind']['direct']+' '+ weather_dict['wind']['power']+'\n湿度：'+str(weather_dict['weather']['humidity'])+'%')
        s.var=var
        w_info=Label(s.frame, textvariable=var, justify=CENTER,bg="white")
        s.w_info=w_info

    def change_city(s, event, c):
        d = get_weather(c)
        s.photo = PhotoImage(file='天气/' + get_image(c))
        s.img_info.configure(image=s.photo)
        if d['wind']['direct'] == '9999':
            s.var.set(d['weather']['info']+'\n实时温度：'+str(d["weather"]["temperature"])+'℃\n'+'-- '+d['wind']['power']+'\n湿度：'+str(d['weather']['humidity'])+'%')
        else:
        	s.var.set(d['weather']['info']+'\n实时温度：'+str(d["weather"]["temperature"])+'℃\n'+d['wind']['direct']+' '+d['wind']['power']+'\n湿度：'+str(d['weather']['humidity'])+'%')


#if __name__ == '__main__':
   #print(get_weather())
#    print(min_max_temp())
 
