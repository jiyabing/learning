
#此处为相对导入
from ..menu import show_menu

#以下导入会报错，因为跳出了package包
#from ...package.meun import show_menu

def play():
    print('正在玩魂斗罗')

def game_over():
    print('游戏结束！')

    #调用menu.py中的show_menu函数
    show_menu()

print('魂斗罗被加载！')
