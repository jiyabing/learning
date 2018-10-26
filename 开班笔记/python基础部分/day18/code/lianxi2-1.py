def input_data():
    l=[]
    while True:
        s = input('输入任意文字：')
        if not s:
            return l 
        l.append(s)


def write_data(l):
    try:
        f = open('input.txt','w')
        for s in l:
            f.write(s)
            f.write('\n') #写入换行符
        print('写入完成！')
        f.close()
    except IOError:
        print('写文件失败')


def main():
    lst = input_data()
    write_data(lst)


main()
