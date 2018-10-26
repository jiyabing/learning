#此示例示意二进制模式读取wenben.txt文件


try:
    f = open('wenben.txt','rb')
    print('打开文件成功')
    #读取文件
    b = f.read()
    print(b)
    s = b.decode('ANSI')
    print('转码后',s)
    f.close()
except IOError:
    print('文件打开失败')
