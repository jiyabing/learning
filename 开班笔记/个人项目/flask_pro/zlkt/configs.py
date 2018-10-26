import os

DEBUG = True

SECRET_KEY = os.urandom(24)
# session过期时间
PERMANENT_SESSION_LIFETIME = 7*24*60*60
# 设置数据库
DIALECT = 'mysql'
DRIVER = 'mysqlconnector'
USERNAME = 'root'
PASSWORD = '123456'
HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlkt_db'
S = '{}+{}://{}:{}@{}:{}/{}?charset=utf8'
SQLALCHEMY_DATABASE_URI = S.format(DIALECT, DRIVER, USERNAME, PASSWORD, HOST, PORT, DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
