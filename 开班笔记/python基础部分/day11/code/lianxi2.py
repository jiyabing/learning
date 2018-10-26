def mymax(x,y):
    if x > y:
        return x
    #else:
        #return y
    return y
print(mymax(24,20))
print(mymax('abc','acd'))

#方法一
'''
def input_number():
    l = []
    while True:
        n = int(input('输入整数：'))
        if n < 0:
            break
        l.append(n)
    return l
'''
#方法一改进
def input_number():
    l = []
    while True:
        n = int(input('输入整数：'))
        if n < 0:
            #break
            return l
        l.append(n)
    #return l

L = input_number()
print('最大值：',max(L))
print('和：',sum(L))
