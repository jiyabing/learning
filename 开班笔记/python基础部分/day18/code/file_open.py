#此程序示意文件的打开和关闭

try:
    file = open('222.py')
    print('打开文件成功')

    

#通常在此进行读写文件内容

#关闭文件
    file.close()
    print('文件以关闭')
    


except IOError:
    print('文件打开失败')
