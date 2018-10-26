class Mylist:
    def __init__(self,iterable):
        self.data = [x for x in iterable]
    def __repr__(self):
        return 'Mylist(%r)' %self.data
    def __add__(self,iterable):
        return Mylist(self.data + iterable.data)
    def __mul__(self,rhn):
        return Mylist(self.data * rhn)
    def __rmul__(self,lhn):
        print('__rmul__被调用,lhn=',lhn)
        return Mylist(self.data * lhn)

l1 = Mylist([1,2,3])
l2 = Mylist(range(4,7))
l3 = l1 + l2
print(l3)
l4 = l1 * 2
print(l4)
l5 = 2 * l2
print(l5)
