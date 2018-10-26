class Biology:  
    def fun(self):
        self.fun_self()

class Animal(Biology):  
    def fun_self(self):
        print("一类动物")

class Dog(Animal):
    def fun_self(self):
        print("一条狗")

def myfun(s):
	s.fun_self()  

s1 = Animal()
myfun(s1)  # 输出结果：
s1 = Dog()
myfun (s1)  #输出结果：


def decdsso(fn):
	print("decdsso")
	def f2():
		print("f2")
	return f2
@decdsso
def myfunc():
	print("myfun!")

myfunc()



def f1():
	v = 200
	def f2():
		v = 300
		def f3():
			nonlocal v
			v = 400
		print('f2.v= ',v ) 
	f2()
	print('f1.v=',v)
f1()
