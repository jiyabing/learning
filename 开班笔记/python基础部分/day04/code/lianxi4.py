n=int(input('输入一个数：'))
#方法一
if n > 0:
	print(n)
else:
	print(-n)
#方法二
if n < 0:
	n = -n
print(n)

#方法三
print(n if n>0 else -n)
