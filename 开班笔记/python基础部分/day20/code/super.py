class A:
	def work(self):
		print('A类的work方法被调用')

class B(A):
	def work(self):
		print('B类的work方法被调用')
	
	def dowork(self):
		self.work() #调用B类的方法
		super(B,self).work() #调用超类的方法
		super().work #一样调用超类的方法

b = B()
b.work() #B类的方法被调用
print('-----以下用b调用覆盖版本的方法-----')
super(B,b).work()
b.dowork()