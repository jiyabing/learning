class A:
	def work(self):
		print('A类的work方法被调用')

class B(A):
	def work(self):
		print('B类的work方法被调用')

b = B()
b.work() #B类的方法被调用