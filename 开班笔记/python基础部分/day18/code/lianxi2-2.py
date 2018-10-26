def read_data(filename):
    f = open(filename)
    l = []
    while True:
        #读取每一行数据
        s = f.readline()
        if not s:
            f.close()
            return l 
        #去掉换行符
        s = s.strip()
        l.append(s) #放入列表
    

def print_file_info(l):
    for s in enumerate(l,1):
        print('第%d行:%s' %s)

def main():
    try:
        lst = read_data('mydata')
        print_file_info(lst)
    except FileNotFoundError:
        print('文件不存在！')

main()
