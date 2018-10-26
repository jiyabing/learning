#mynumber.py

#此程序示意运算符重载
class Mynumber:
    def __init__(self,v):
        self.data = v
    def __repr__(self):
        return 'Mynumber(%d)' %self.data
    def __add__(self,other):
        print('__add__方法被调用')
        obj = Mynumber(self.data + other.data)
        return obj
    def __sub__(self,other):
        obj = Mynumber(self.data - other.data)
        return obj
    def __mul__(self,other):
        return Mynumber(self.data * other.data)
        



n1 = Mynumber(100)
n2 = Mynumber(200)
#n3 = n1.__add__(n2)
n3 = n1 + n2 #等同于n1.__add__(n2)
print(n3)
n4 = n1 - n2
print(n4)
