def myfun(a,*,k):
    print('a=',a)
    print('k=',k)

#myfun(1,2)#报错
myfun(1,k=2)#k强制使用关键字传参
myfun(10,**{'k':20})

def myfun2(b,*args,c,d):
    print('b=',b)
    print('args=',args)
    print('c=',c)
    print('d=',d)

myfun2(1,2,3,4,c=5,d=6)
