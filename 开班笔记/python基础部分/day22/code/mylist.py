#此示例示意复合赋值算术运算符重载
class Mylist:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'Mylist(%r)' %self.data

    def __add__(self,iterable):
        print('__add__方法被调用')
        return Mylist(self.data + iterable.data)

    def __iadd__(self,iterable):
        print('__iadd__方法被调用')
        self.data.extend(iterable.data)
        return self

l1 = Mylist([1,2,3])
l2 = Mylist(range(4,7))
l1 += l2 #相当于l1 = l1 + l2
print(l1)
