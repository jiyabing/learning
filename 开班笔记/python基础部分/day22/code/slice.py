#此示例示意in/not in 重载
class Mylist:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'Mylist(%r)' %self.data

    def __getitem__(self,i):
        print('__getitem__被调用',i)
        if type(i) is slice:
            print('正在进行切片操作')
        elif type(i) is int:
            print('正在进行索引操作')
        return self.data[i]

    def __setitem__(self,i,v):
        print('__setitem__被调用')
        self.data[i] = v

    #def __delitem__():



l1 = Mylist([1,-2,3,-4,5])
print(l1[2])
l1[1] = 2
print(l1)
print(l1[::2]) #调用__getitem__方法 l1[::2]等同于l1(slice(None,None,2))
