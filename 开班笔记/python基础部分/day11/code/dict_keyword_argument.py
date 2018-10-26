#此示例示意双星号字典形参的用法：
def func(**kwargs):
    print('关键字传参的个数：',len(kwargs))
    print('kwargs=',kwargs)

func(name='tarena',age=15)
func(a=1,b='abc',c=[1,23,3],d=True)
