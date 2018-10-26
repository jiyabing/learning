#myzip.py

#此示例示意zip函数的内部实现方法
def myzip(iter1,iter2):
    it1 = iter(iter1)
    it2 = iter(iter2)
    try:
        while True:
            a = next(it1)
            b = next(it2)
            yield (a,b)
    except:
        pass



number = [1,2,3]
name = ('a','b','c','d')

for i in myzip(number,name):
    print(i)
