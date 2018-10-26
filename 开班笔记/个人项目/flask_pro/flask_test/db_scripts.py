"""
所有数据库的相关操作
"""

from flask_script import Manager

DBManage = Manager()


@DBManage.command
def init():
    print('数据库初始化成功')


def migrate():
    print('数据库迁移成功')
