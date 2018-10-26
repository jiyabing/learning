class Human:
	def __init__(self,n,a):
		print('Human类的__init__被调用')
		self.name = n
		self.age = a
		
	
	def show_info(self):
		print('Human类的show_info被调用')
		print('姓名：',self.name)
		print('年龄：',self.age)


class Student(Human):
	def __init__(self,n,a,s):
		super().__init__(n,a)#显示调用基类的初始化方法
		self.score = s
		print('Student类的__init__被调用')
	
	def show_info(self):
		super().show_info() #调用基类的show_info方法
		print('成绩：',self.score)

s1 = Student('张',40,100)
s1.show_info()