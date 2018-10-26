v = 1
def fx():
    global v#声明v为全局变量，不是局部变量
    v = 2

fx()
print(v)
