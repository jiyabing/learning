'''
print('第一题')
def mysum(*args):
    return sum(args)
print(mysum(1,3,36,3))
'''    

print('第二题')
#方法一
def mymax(*args):
    if len(args) == 1:
        l = list(*args)
        l.sort()
        return l[-1]
        #return max(args[0])
    return max(args)

#方法二
def mymax2(a,*args):
    if len(args) == 0:
        m = a[0] #先假设第一个数最大
        i = 1
        while i < len(a):#遍历之后的每一个元素
            if a[i] > m:
                m = a[i]
            i += 1
        return m
    else:
        m = a
        for x in args:
            if x > m:
                m = x
        return m

#方法三：
def mymax3(a,*args):
    def _max(*args):
        m = args[0]
        i = 1
        while i < len(args):
            if args[i] > m:
                m = args[i]
            i += 1
        return m

    if len(args) == 0:
        return _max(*a)
    return _max(a,*args)
        
    

print(mymax([1,2,3]))
#print(mymax(100,200))
#print(mymax('abc'))
#print(mymax('c','f','g'))
#print(mymax([1,23,4],[3,4,5]))
#print(mymax(1,[2,3]))

'''
print('第三题')
def min_max(*args):
    t = (min(args),max(args))
    return t

print(min_max(1,2,3,4))
'''    
