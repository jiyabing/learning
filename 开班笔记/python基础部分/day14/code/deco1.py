
#装饰器函数
def mydeco(fn):
    def fx():
        print('hello world')
        fn()
        print('-----------')
    return fx



@mydeco
def hello():#被装饰函数
    print('hello tarena')

#此时将hello变量绑定在了mydeco返回的函数上
#hello=mydeco(hello) #此种做法可以用装饰器@语法解决

hello()


'''
#存钱对应的函数
#以下是一个装饰器函数，在fn调用之前加一个权限验证的功能
def priv_check(fn):
    def fx(name,x):
        print('正在权限验证...')
        fn(name,x)
    return fx

#余额变动提醒函数装饰器
def message_send(fn):
    def fy(name,x):
        #先办理业务
        fn(name,x)
        print(name,'发生了',x,'元的操作，余额是xxx')
    return fy


#存钱
@priv_check
def save_money(name,x):
    print(name,'存钱',x,'元')

@message_send #修饰(@priv_check和withdraw) 
@priv_check #修饰withdraw
def withdraw(name,x):#取钱
    print(name,'正在办理取钱',x,'元的业务')

save_money('小张',200)
save_money('小赵',500)


withdraw('小李',300)
'''
