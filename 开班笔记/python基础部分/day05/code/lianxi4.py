s = input('输入任意一串字符：')
if s:
	print('第一个字符的Unicode码是：',ord(s[0]))
else:
	print('字符为空')

n = int(input('输入一个整数(0~65535)：'))
print(chr(n))
