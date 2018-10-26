class Calltest():
	def __call__(self,a,b):
		print('This is call test')
		print(a,b)

test = Calltest()
test(1,2)