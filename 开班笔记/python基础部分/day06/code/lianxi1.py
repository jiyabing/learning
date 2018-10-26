s1 = input('请输入第一行：')
s2 = input('请输入第二行：')
s3 = input('请输入第三行：')
l = max(len(s1),len(s2),len(s3))

#方法一
print('%*s\n%*s\n%*s' %(l,s1,l,s2,l,s3))

#方法二
fmt = '%'+str(l)+'s' # or fmt = '%%%ds' %l
print(fmt %s1)
print(fmt %s2)
print(fmt %s3)
