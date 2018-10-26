from exts import db


class User(db.Model):
    """创建用户表模型"""
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    age = db.Column(db.Integer)


# 创建文章标签表(多对多)
article_tag = db.Table('article_tag',
                       db.Column('article_id', db.Integer, db.ForeignKey('article.id'), primary_key=True),
                       db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True)
                       )


class Article(db.Model):
    """创建文章表模型"""
    # 定义表名，固定语法
    __tablename__ = 'article'
    # 定义字段及属性
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 整型，主键，自增
    title = db.Column(db.String(128), nullable=False)  # varchar
    content = db.Column(db.Text, nullable=False)  # text文本型
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # user.id必须是表的名字，不能是User.id
    # 创建作者和文章间的关系，方便查找
    author = db.relationship('User', backref=db.backref('articles'))
    # 创建标签和文章间的关系
    tags = db.relationship('Tag', secondary=article_tag, backref=db.backref('articles'))


class Tag(db.Model):
    """创建标签表模型"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
