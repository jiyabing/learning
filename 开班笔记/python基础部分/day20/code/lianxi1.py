class Human:
    count = 0 #类变量

    def __init__(self,n,a,addr):
        self.name = n
        self.age = a
        self.id = addr
        self.__class__.count += 1 #修改类变量


    def __del__(self):
        self.__class__.count -= 1

    @classmethod
    def get_human_count(cls):
        return cls.count


    def show_info(self):
        print('''姓名:%s 年龄:%d 家庭住址:%s''' %(self.name,self.age,self.id))


    def updata_age(self):
        self.age += 1

def input_human():
    lst = []
    while True:
        n = input('输入姓名:')
        if not n:
            break
        a = int(input('输入年龄：'))
        addr = input('请输入地址:')
        if not addr:
            addr = '未填写'
        h = Human(n,a,addr)
        
            
        lst.append(h)
    return lst


def main():
    docs = input_human()
    print('当前的总人数是',Human.get_human_count())
    for h in docs:
        h.show_info()
    for h in docs:
        h.updata_age()
    for h in docs:
        h.show_info()

main()
