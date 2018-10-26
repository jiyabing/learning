n=int(input('季度：'))
if n == 1:
	print(1,2,3)
elif n == 2:
	print(4,5,6)
elif n == 3:
	print(7,8,9)
elif n == 4:
	print(10,11,12)
else:
	print('输错了')


m=int(input('月份：'))
if 1 <= m <= 3:
	print('一季度')
elif 4 <= m <= 6:
	print('二季度')
elif 7 <= m <= 9:
	print('三季度')
elif 10 <= m <= 12:
	print('四季度')
else:
	print('输入月份有误')

