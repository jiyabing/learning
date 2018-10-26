m=int(input('月份：'))
if 1 <= m <= 12:
	if m <= 3:
		print('春季')
	elif m <= 6:
		print('夏季')
	elif m <=9:
		print('秋季')
	else:
		print('冬季')
else:
	print('输入有误')
