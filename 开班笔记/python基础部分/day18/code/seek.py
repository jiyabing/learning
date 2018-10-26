f = open('alpha_number.txt','rb') #二进制打开
f.read(5)

#f.seek(10,0) #将光标从文件头向右移动了10位

f.seek(5,1)#将光标从当前位置向右移动了5位

#f.seek(-10,2)#将光标从文件尾向作移动了10位

b = f.read(5)
print(b)
f.close()
