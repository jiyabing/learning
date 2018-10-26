from flask import Flask, render_template, session
import configs
from exts import db


app = Flask(__name__)
# 导入配置文件
app.config.from_object(configs)
# 初始化
db.init_app(app)


@app.route('/session/')
def ses():
    session['username'] = 'zhangsan'
    session.permanent = True
    return session.get('username')


@app.route('/db/')
def data():
    """数据库的增删改查"""
    # 增
    # article1 = Article(title='aaa', content='bbb')  # 创建数据实例
    # db.session.add(article1)  # 增加数据的事务操作
    # db.session.commit()  # 提交事务

    # user1 = User(username='zhang')
    # # 方法一，添加文章，关联作者id
    # article1 = Article(title='aaa', content='bbb', author_id=1)
    # # 方法二，将文章关联到作者“zhang”上
    # article2 = Article(title='ccc', content='ddd')
    # article2.author = User.query.filter(User.username == 'zhang').first()
    # db.session.add(user1)
    # db.session.add(article1)
    # db.session.add(article2)
    # db.session.commit()
    # 增加文章并添加标签
    # article3 = Article(title='a', content='nihao', author_id=1)
    # article4 = Article(title='b', content='hello world', author_id=1)
    # tag1 = Tag(name='111')
    # tag2 = Tag(name='222')
    # article3.tags.append(tag1)
    # article3.tags.append(tag2)
    # article4.tags.append(tag1)
    # db.session.add(article3)
    # db.session.add(article4)
    # db.session.add(tag1)
    # db.session.add(tag2)
    # db.session.commit()

    # 查
    # articles = Article.query.filter(Article.title == 'aaa').all()  # 返回的是Query对象列表(first()可取第一个)
    # for i in articles:
    #     print({'title': i.title, 'content': i.content})  # i.title表示i对象的title属性值
    # # 查找文章标题aaa的作者姓名
    # article = Article.query.filter(Article.title == 'aaa').first()
    # print(article.author.username)
    # # 查找作者zhang写的所有文章
    # user = User.query.filter(User.username == 'zhang').first()
    # result = user.articles
    # for i in result:
    #     print(i.title)
    # 查找文章标题为a下的所有标签
    # article = Article.query.filter(Article.title == 'a').first()
    # result = article.tags
    # for i in result:
    #     print(i.name)

    # 改
    # # 1.找出要修改的数据
    # article1 = Article.query.filter(Article.title == 'aaa').first()
    # # 2.修改数据内容
    # article1.title = 'ccc'
    # article1.content = 'ddd'
    # # 3.提交事务
    # db.session.commit()

    # 删
    # # 1.找出要删除的数据
    # article2 = Article.query.filter(Article.title == 'ccc').first()
    # # 2.删除数据
    # db.session.delete(article2)
    # # 3.提交事务
    # db.session.commit()
    return 'hello world'


@app.route('/<is_login>')
def index(is_login):
    class Person(object):
        name = '包拯'
        age = 45

    context = {
        'username': u'知了课堂',
        'sex': u'男',
        'age': 18,
        'Person': Person,
        'websites': {
            'baidu': 'www.baidu.com',
            'sina': 'www.sina.com.cn'
        }
    }
    if is_login == '1':
        return render_template('index.html', context=context)
    else:
        return render_template('index.html')


@app.route('/books/')
def for_book():
    books = [
        {
            'name': '三国演义',
            'price': 200
        },
        {
            'name': '红楼梦',
            'price': 200
        },
        {
            'name': '水浒传',
            'price': 200
        },
        {
            'name': '西游记',
            'price': 200
        }
    ]
    return render_template('books.html', books=books)


if __name__ == '__main__':
    app.run()
