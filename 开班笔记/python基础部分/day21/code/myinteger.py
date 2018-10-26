#此示例示意abs(obj)函数的重写方法obj.__abs__()方法的使用
class Myinteger:
	def __init__(self,value):
		self.data = value
	def __repr__(self):
		return 'Myinteger(%d)' %self.data
	
	def __abs__(self):
		if self.data < 0:
			return Myinteger(-self.data)
		return Myinteger(self.data)
	
	def __len__(self):
		'''len(x)函数只能返回整数值，因此此方法不能返回字符串等其他类型的值'''
		return 100


I1 = Myinteger(-10)
print(I1)  #<---此处等同于print(str(I1))
I2 = abs(I1)
print(I2)
print(len(I2))