import requests
from bs4 import BeautifulSoup
from tkinter import *
import webbrowser

url = 'http://news.sina.com.cn/china'


def getNews():
    res = requests.get(url)
    # 使用UTF-8编码
    res.encoding = 'UTF-8'

    # 使用剖析器为html.parser
    soup = BeautifulSoup(res.text, 'html.parser')

    newslist = []

    # 遍历每一个class=b1k121的节点
    for news in soup.select('.blk121'):
        # 遍历出节点中每一个a标签
        for a in news.find_all('a'):
            href = a['href']
            title = a.string
            newslist.append(title + '#' + href)
            # print('标题：',title,'链接：',href)
    return newslist


# if __name__ == "__main__":
#   for i in getNews():
#     print(i.split('#')[0])
#     print(i.split('#')[1])
class News_text:
    def __init__(s, frame):
        s.frame=frame
        s.newsurl = []
        s.newstext = []
        s.newsText()
        s.show_newstext()

    def newsText(s):  # 创建Text控件
        for i in getNews():  # 将每条新闻的标题和链接分别存储
            s.newstext.append(i.split('#')[0])
            s.newsurl.append(i.split('#')[1])
        news_l = Text(s.frame, font=('宋体', 10),height=4,width=40)  # 创建控件并设置
        s.news_l = news_l
        news_l.tag_config('link', foreground='#0066FF', underline=True)
        news_l.config(cursor='arrow')

    def click(s, event, x):
        webbrowser.open(x)

    def handlerAdaptor(s, fun, **kwds):
        return lambda event, fun=fun, kwds=kwds: fun(event, **kwds)

    def show_newstext(s):
        m = 0
        for each in s.newstext:
            s.news_l.tag_config(m, foreground='#0066FF')
            s.news_l.insert(INSERT, each + '\n', m)
            s.news_l.tag_bind(m, '<Button-1>', s.handlerAdaptor(s.click, x=s.newsurl[m]))
            m += 1
        s.news_l.config(state=DISABLED)