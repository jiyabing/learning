#此程序示意文件的读写

try:
    file = open('wenben.txt')
    print('打开文件成功')

    

#通常在此进行读写文件内容
    s = file.readline()
    print('第一行的内容是：',s)
    s = file.readline()
    print('第二行的内容是：',s)
    s = file.readline()
    print('第三行的内容是：',s)
    print(file.readlines())

#关闭文件
    file.close()
    print('文件以关闭')
    


except IOError:
    print('文件打开失败')
