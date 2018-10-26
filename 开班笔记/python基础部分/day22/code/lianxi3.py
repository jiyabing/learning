class OrderSet:
    def __init__(self,iterable):
        self.data = [x for x in iterable]

    def __repr__(self):
        return 'OrderSet(%r)' %self.data

    def __and__(self,other):
        return OrderSet(set(self.data) & set(other.data))

    def __or__(self,other):
        return OrderSet(set(self.data) | set(other.data))

    def __sub__(self,other):
        return OrderSet(set(self.data) - set(other.data))

    def __xor__(self,other):
        return OrderSet(set(self.data) ^ set(other.data))

    def __eq__(self,other):
        if self.data == other.data:
            return True
        return False

    def __ne__(self,other):
        if self.data  != other.data:
            return True
        return False


s1 = OrderSet([1,2,3,4])
s2 = OrderSet([3,4,5])
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)
if OrderSet([1,2,3]) != OrderSet([1,2,3,4]):
    print('不相同')
else:
    print('相同')
