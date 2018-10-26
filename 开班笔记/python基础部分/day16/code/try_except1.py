#此示例示意用try-except语句来捕获异常
def div_apple(n):
    '此示例用分苹果来示意捕获异常'
    print('%d个苹果你想要分给几个人？' %n)
    s = input('输入人数：')
    cnt = int(s)  #<--此处可能会引起ValueError类型的错误
    result = n / cnt #<--此处可能会引起ZeroDivisionError类型的错误
    print('每人分了',result,'个苹果')


try:
    div_apple(10)


#第一种
except ValueError:
    print('发生了值错误，以转为正常状态')
except ZeroDivisionError:
    print('发生了被零除的错误')


#也可如下：
except (ValueError,ZeroDivisionError):
    print('发生错误')

except:
    print('其他的所有异常都有我来处理')

else:
    #此处语句只有在没有发生异常时才会执行
    print('没有错误发生，苹果分完')

finally:
    print('有或没有异常，都会执行')    

print('程序正常退出')
