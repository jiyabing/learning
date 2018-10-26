class Mylist:
	'''定义一个容器类，用于存储任意类型的数据，
	   其内部的存储方式用list实现'''
	def __init__(self,iterable):
			self.data = [x for x in iterable]
		
	def __repr__(self):
			return 'Mylsit(%s)' %self.data
	
	def __iter__(self):
		'''此方法把Mylist类型的对象做为可迭代对象使用，此方法需要
		   返回迭代器'''
		#return iter(self.data)
		return MylistIterator(self.data)
	
class MylistIterator:
	'''此类定义一个迭代器类，用于生成能够访问Mylist对象的迭代器'''
	def __init__(self,lst_data):
		print('迭代器已经创建')
		self.data = lst_data #绑定要访问的数据列表
		self.cur_pos = 0 #设置迭代器的起始位置为0
	def __next__(self):
		'''此方法用来访问可迭代对象的数据，如果没有数据时触发StopIterator
		   异常来通知调用这停止迭代，即‘迭代器协议’'''
		#判断是否索引越界
		if self.cur_pos >= len(self.data):
			raise StopIteration
		index = self.cur_pos
		self.cur_pos += 1 #将当前位置向后移动一位准备下次获取
		return self.data[index] #返回当前位置的数据
		
myl = Mylist([1,3,4,5,10])
for x in myl:
	print(x)