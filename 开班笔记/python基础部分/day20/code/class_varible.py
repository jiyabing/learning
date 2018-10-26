#class_varible.py


#此示例示意类变量的用途和使用方法

class Human:
    total_count = 0
    def __init__(self,name):
        self.name = name
        self.__class__.total_count += 1 #人数加1
        print(name,'对象创建')


    def __del__(self):
        self.__class__.total_count -= 1 #总人数减1


print('当前对象的个数是：',Human.total_count)
h1 = Human('张飞')
h2 = Human('赵云')
print('当前对象的个数是：',Human.total_count)
del h1
print('当前对象的个数是：',Human.total_count)


