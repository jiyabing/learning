#此示例示意以二进制方式打开文件后进行写操作

f = open('bindata.txt','wb')
print('文件打开')

f.write(b'hello') #写入五个字节

s = '我是汉字'
c = f.write(s.encode('ANSI')) #返回写入字节的数量，可用变量绑定
print('%d个字节' %c)

f.close()
