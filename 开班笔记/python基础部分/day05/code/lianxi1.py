n = int(input('请输入矩形宽度：'))
if n > 2:
	print('#' * n)
	print('#'+' ' * (n-2)+'#')
	print('#'+' ' * (n-2)+'#')
	print('#' * n)
else:
	print('#' * 2)
	print('#' * 2)
