from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app
from models import *

manage = Manager(app)
# 使用migrate绑定app和db
migrate = Migrate(app, db)
# 添加迁移脚本到manage中
manage.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manage.run()
