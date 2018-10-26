from flask import Flask, render_template, request, redirect, url_for, session
import configs
from models import *
from functools import wraps

app = Flask(__name__)
app.config.from_object(configs)
db.init_app(app)


# 登录限制装饰器
def login_require(func):
    @wraps(func)  # 防止更改func.__name__, 固定格式
    def wrapper(*args, **kwargs):
        if session.get('user_id'):
            return func(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrapper


@app.route('/')
def index():
    questions = Question.query.order_by('-create_time').all()
    return render_template('index.html', questions=questions)


@app.route('/login/', methods=('GET', 'POST'))
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        phone = request.form.get('phone')
        pwd = request.form.get('password')
        result = User.query.filter(User.phone == phone, User.password == pwd).first()
        if result:
            session['user_id'] = result.id
            session.permanent = True
            return redirect(url_for('index'))
        else:
            message = '用户名或密码不正确'
            return render_template('login.html', message=message)


@app.route('/logout/')
def logout():
    # session.pop('user_id')
    # del session['user_id']
    session.clear()
    return redirect(url_for('login'))


@app.route('/register/', methods=('GET', 'POST'))
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        phone = request.form.get('phone')
        result = User.query.filter(User.phone == phone).first()
        if result:
            message = '该手机号已注册'
            return render_template('register.html', message=message)
        username = request.form.get('username')
        pwd1 = request.form.get('password1')
        pwd2 = request.form.get('password2')
        if pwd1 != pwd2:
            message = '两次密码不一致'
            return render_template('register.html', message=message)
        user = User(phone=phone, username=username, password=pwd1)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))


# 钩子函数，上下文
@app.context_processor
def my_context():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {'user': user}
    return {}  # 必须要返回一个字典，即使是空


@app.route('/question/', methods=('GET', 'POST'))
@login_require  # 先进行登录判断
def question():
    if request.method == 'GET':
        return render_template('question.html')
    else:
        # 获取当前登录用户
        user_id = session.get('user_id')
        user = User.query.filter(User.id == user_id).first()
        # 获取问题和回答
        title = request.form.get('title')
        content = request.form.get('content')
        # 方法一
        # new_question = Question(title=title, content=content, user_id=user.id)

        # 方法二
        new_question = Question(title=title, content=content)
        new_question.user = user

        db.session.add(new_question)
        db.session.commit()
        return redirect(url_for('index'))


@app.route('/detail/<question_id>')
def detail(question_id):
    result = Question.query.filter(Question.id == question_id).first()
    return render_template('detail.html', question=result)


@app.route('/comment/', methods=('POST',))
@login_require
def comment():
    user_id = session.get('user_id')
    user_model = User.query.filter(User.id == user_id).first()
    content = request.form.get('comment')
    question_id = request.form.get('question_id')
    question_model = Question.query.filter(Question.id == question_id).first()
    new_comment = Comment(comment=content)
    new_comment.user = user_model  # 绑定该条评论的用户id
    new_comment.question = question_model  # 绑定该条评论的问题id
    db.session.add(new_comment)
    db.session.commit()
    return redirect(url_for('detail', question_id=question_id))


if __name__ == '__main__':
    app.run()
