# 1、如何创建队列。=[]
# 2、在队列中增加一个元素
# 3、在队列的尾部删除一个元素。
# 4、判断队列是不是为空
# # 5、计算队列的长度。
class Queue(object):
    def __init__(self):
        self.item = []
#在列表的头位置增加元素

    def enqueue(self,i):
        self.item.insert(0,i)
#在列表的尾部删除元素
    def dequeue(self):
        return self.item.pop()

    def is_empty(self):
        return self.item == []

    def size(self):
        return len(self.item)

L=Queue()
print(L.is_empty())
L.enqueue("hello")
L.enqueue("world")
print(L.is_empty())
print(L.dequeue())
print(L.size())
L.dequeue()
print(L.is_empty())







