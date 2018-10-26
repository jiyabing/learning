#! /usr/bin/python3

# file   : game2048py
# author : 魏明择
# date   : 2018


import random


map2048 = [[2, 0, 2, 4],
           [2, 2, 4, 4],
           [2, 0, 0, 4],
           [4, 0, 4, 8]]


# 重新设置开始游戏的地图
def reset():
    global map2048
    map2048 = [[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]]
    fill_to_zero(2)
    fill_to_zero(2)
    fill_to_zero(4)


# 算法1
# 去除列表中的所有0
def _remove_zero(L):
    try:
        while True:
            i = L.index(0)
            # 否则将i指向的位置删除
            L.pop(i)
    except ValueError:  # 结束执行删除0
        pass


# 移动一行数据,自右至左滑动算法
def _left_shift(L):
    old = L.copy()
    # 第一步，将0全部删除
    _remove_zero(L)
    # 第二步，合并相邻两个相同值的元素，
    # 将左侧值做乘2操作，将右侧的值置0
    for i in range(len(L) - 1):  # 重复最多3次
        if L[i] == L[i + 1]:
            L[i] *= 2
            L[i + 1] = 0
    # 第三步，再次删除0
    _remove_zero(L)
    # 第四步，在长度不足4的列表中尾部添加0
    while len(L) < 4:
        L.append(0)
    # 当新的列表与旧列表不同时，返回True
    # 否则返回False
    return L != old


# 左操作，将每一行都执行左移操作
def left():
    ret = False
    for r in map2048:
        if _left_shift(r):
            ret = True
    return ret  # ret (urn)


# 右操作，
def right():
    # 先将所有行左右反转
    for r in map2048:
        r.reverse()
    # 再左移操作，
    ret = left()
    # 再左右反转回来
    for r in map2048:
        r.reverse()
    return ret


# 上操作
def up():
    ret = False
    # 对每一列进行操作,i代表列索引
    for i in range(4):
        L = []
        for r in map2048:
            # 将每一行的第i列放入列表
            L.append(r[i])
        if _left_shift(L):
            ret = True
        # 再将列表入回原列中
        for j in range(4):
            map2048[j][i] = L[j]
    return ret


# 下操作
def down():
    map2048.reverse()
    ret = up()
    map2048.reverse()
    return ret


def fill_to_zero(n):
    L = []
    for r in range(4):
        for c in range(4):
            if map2048[r][c] == 0:
                L.append((r, c))
    # 如果L 为空，则没有空位置，直接返回
    if not L:
        return
    # 随机选择列表中的一个元素
    i = random.choice(L)
    r, c = i  # 元组序列赋值
    map2048[r][c] = n
    # print(L)


def is_gameover():
    """判断是否已经游戏结束"""
    # 遍历所有的行
    for r in map2048:
        # 如果行中出现0则,游戏没有结束
        if r.count(0):
            return False
    # 每一行中的相邻元素相同，则游戏没有结束
    for r in map2048:
        for i in range(len(r) - 1):
            if r[i] == r[i + 1]:
                return False
    # 每一列中的相邻元素相同，则游戏没有结束
    for col in range(4):  # col 为列
        for i in range(3):  # 行索引
            if map2048[i][col] == map2048[i + 1][col]:
                return False
    # 以上都没有，则游戏失败
    return True


# 初始化地图
reset()


# 用来显示2048界面和相应操作
clr = {
    0: "\033[0;30;47m",
    2: "\033[0;30;43m",
    4: "\033[0;30;42m",
    8: "\033[0;30;46m",
    16: "\033[0;30;45m",
    32: "\033[0;30;41m",
    64: "\033[0;30;44m",
    128: "\033[1;30;47m",
    256: "\033[1;37;43m",
    512: "\033[1;37;42m",
    1024: "\033[1;37;46m",
    2048: "\033[1;37;45m",
}


def show_map():
    """在控制台终端上显示2048操作界面"""
    for r in map2048:
        for c in r:
            print(clr[c] + '      ', end=' ')
        print('\033[0m')  # 重置控制台终端

        for c in r:
            text = str(c) if c else ''
            print(clr[c] + text.center(6), end=' ')
        print('\033[0m')  # 重置控制台终端

        for c in r:
            print(clr[c] + '      ', end=' ')
        print('\033[0m')  # 重置控制台终端


def main():
    while not is_gameover():  # 如果游戏没有gameover将继续
        show_map()
        key = input("a: 左\nd: 右\nw: 上\ns: 下\nq: 退出\n请输入操作: ")
        if 'a' == key:
            if left():  # 左操作
                fill_to_zero(2)
        elif 'd' == key:
            if right():  # 右操作
                fill_to_zero(2)
        elif 'w' == key:
            if up():  # 上操作
                fill_to_zero(2)
        elif 's' == key:
            if down():  # 下操作
                fill_to_zero(2)
        elif 'q' == key:
            exit()


if __name__ == '__main__':
    main()



