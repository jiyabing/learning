#classmethod.py
class A:
    v = 0
    @classmethod
    def get_v(cls):
        return cls.v

    @classmethod
    def set_v(cls,value):
        cls.v = value

print(A.get_v()) #0

A.v = 1
print(A.get_v()) #1

A.set_v(100)
print(A.get_v()) #100

a = A()
a.set_v(200)
print(A.get_v())
