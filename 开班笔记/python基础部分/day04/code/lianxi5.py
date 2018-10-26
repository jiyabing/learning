'''
print('第一题')
k=int(input('请输入公里数：'))
if k > 15:
	pay = 13 + 12*2.3 + (k-15)*(2.3+1.15)
elif 3 < k <= 15:
	pay = 13 + (k-3)*2.3
else:
	pay = 13
print('应付车费：',round(pay))
'''

'''
print('第二题')
#方法一
s1=int(input('1:'))
s2=int(input('2:'))
s3=int(input('3:'))
Max,Min = s1, s2
if s1 > s2:
	pass
else:
	Max,Min = s2, s1
if Max > s3:
	if Min > s3:
		Min = s3
else:
	Max = s3
print('最高：', Max,'最低：',Min)
'''

'''
#方法二
l=[]
for i in range(3):
	s = int(input('请输入成绩：'))
	l.append(s)
print('最高：',max(l),'最低：',min(l))
'''
'''
#方法三
Max = s1
if Max < s2:
	Max = s2
if Max < s3:
	Max = s3
print('最高：',Max)
'''


'''
print('第三题')
y = int(input('请输入年份：'))
if (y%4 == 0 and y%100 != 0) or y%400 == 0:
	print(y,'是闰年')
else:
	print(y,'是平年')
'''

'''
print('第四题')
h = float(input('请输入身高：'))
w = int(input('请输入体重：'))
BMI = round(w/h**2,2)
if BMI > 24:
	print(BMI,'体重过重')
elif 18.5 <= BMI <= 24:
	print(BMI,'正常范围')
else:
	print(BMI,'体重过轻')
'''




