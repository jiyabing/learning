#本示例示意with语句的使用方法
with open('abcd.txt') as f:
    while True:
        s = f.readline()
        if not s:
            break
        int(input('输入任意数字打印下一行：'))
        print(s.strip())

