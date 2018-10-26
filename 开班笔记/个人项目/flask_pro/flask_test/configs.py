import os

# 开启debug模式
DEBUG = True

# 配置mysql数据库
# 固定格式
# dialect+driver://username:password@host:port/database
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask_db'
S = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'
SQLALCHEMY_DATABASE_URI = S.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False

# session设置
SECRET_KEY = os.urandom(24)  # '24位字符的字符串'
# 有效期为七天，默认为31天
PERMANENT_SESSION_LIFETIME = 7*24*60*60
