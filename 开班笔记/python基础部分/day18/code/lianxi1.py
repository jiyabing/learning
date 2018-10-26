def read_data():
    try:
        f = open('data.txt')
        d = {}
        while True:
            s = f.readline()
            if not s:
                f.close()
                return d
            s = s.rstrip()
            l = s.split()
            d[l[0]] = l[-1]
    except IOError:
        print('读取文件失败！')


def out_data():
    for k in read_data():
        print('姓名：%-3s 电话：%s' %(k,read_data()[k]))

out_data()
        
    
