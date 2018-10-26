y=int(input('请输入年数：'))
w=(y*365)//7
d=(y*365)%7
print('%r周余%r天' %(w,d))


h=int(input('时：'))
m=int(input('分：'))
s=int(input('秒：'))
sum=h*3600+m*60+s
print(sum)

