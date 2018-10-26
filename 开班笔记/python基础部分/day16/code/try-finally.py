#此示例示意try-finally语句的用法：
#打开天然气后必须关闭天然气
def fry_egg():
    print('打开天然气！')
    try:
        try:
            count = int(input('输入鸡蛋个数：'))
            print('完成煎鸡蛋！共煎了%d个鸡蛋' %count)
        finally:
            print('关闭天然气')
    except ValueError:
        print('程序转为正常')

fry_egg()

print('程序正常退出')
