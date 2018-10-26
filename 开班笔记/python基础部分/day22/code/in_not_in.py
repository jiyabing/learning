#此示例示意in/not in 重载
class Mylist:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'Mylist(%r)' %self.data

    def __contains__(self,e):#e代表测试元素
        print('__contains__被调用')
        for x in self.data:
            if e == x: #如果相同，说明e在列表中
                return True
        return False



l1 = Mylist([1,-2,3,-4,5])

if 2 in l1: #需要重载in函数
    print('2在l1中')
else:
    print('2不在l1中')
