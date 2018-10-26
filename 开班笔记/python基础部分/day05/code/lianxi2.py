s = input('请输入一串字符串：')
print(s[0])
print(s[-1])
if len(s)%2 == 0:
	print("'|'")
else:
	print(s[len(s)//2])
