class MyList(list):
	def insert_head(self,element):
		#self[0:0] = [element]
		self.insert(0,element)


myl = MyList([3,4,5,6])
print(myl)

myl.insert_head(1)
print(myl)