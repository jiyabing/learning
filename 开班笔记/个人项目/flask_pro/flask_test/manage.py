from flask_script import Manager
from app import app
from db_scripts import DBManage
from exts import db
from flask_migrate import Migrate, MigrateCommand
from models import *

manage = Manager(app)
# 要使用flask_migrate,必须绑定app,db
migrate = Migrate(app, db)


@manage.command
def runserver():
    print('服务器跑起来了')


# 将DBManage中的命令到manage
# 将MigrateCommand命令添加到manage
# manage.add_command('db', DBManage)
manage.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manage.run()
