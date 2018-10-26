import hashlib
import json, pymysql, time
from os import remove

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, UIModule

from Tornado.day04.util.myutil import mymd5
from Tornado.day05.app.myapp import MyApplication
from Tornado.day05.util.dbutil import DBUtil


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        r = ''
        msg = self.get_query_argument('msg', None)
        if msg:
            r = '用户名或密码错误'
        self.render('login.html', result=r)

    def post(self, *args, **kwargs):
        pass


class LoginHandler(RequestHandler):
    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        name = self.get_body_argument('user')
        password = self.get_body_argument('pwd')
        pwd = mymd5(password)

        # dbutil = DBUtil()
        if self.application.dbutil.isloginsuccess(name, pwd):
            self.redirect('/blog?user='+name)
        else:
            self.redirect('/?msg=用户信息不正确')


class BlogHandler(RequestHandler):
    '''
    def set_default_headers(self):
        # 让继承者自定义响应头中的内容
        print('set_default_headers方法被调用')

    def initialize(self):
        # 让继承者在执行get/post方法之前传入必要的参数
        # 或者执行一些初始化操作
        print('initialize方法被调用')

    def on_finish(self):
        # 执行get/post方法执行完毕后，释放资源
        print('on_finish方法被调用')
    '''

    def get(self, *args, **kwargs):
        print('get方法被调用')
        self.render('blog.html',
                    blogs=[{
                        'author': '王宝强',
                        'avatar': None,
                        'title': '我被绿了？',
                        'content': '的发阿飞啊士大夫士大夫我似的发额阿道夫阿斯蒂芬完全啊',
                        'tags': '出轨 绿帽子',
                        'count': 1000},
                        {
                            'author': '贾乃亮',
                            'avatar': '111.jpg',
                            'title': '我被绿了？',
                            'content': '的发阿飞啊士大夫士大夫我似的发额阿道夫阿斯蒂芬完全啊',
                            'tags': '出轨 绿帽子',
                            'count': 1000
                        },
                        {
                            'author': '陈羽凡',
                            'avatar': 'a.jpg',
                            'title': '我被绿了？',
                            'content': '的发阿飞啊士大夫士大夫我似的发额阿道夫阿斯蒂芬完全啊',
                            'tags': '出轨 绿帽子',
                            'count': 0
                        },
                    ])

    def post(self, *args, **kwargs):
        pass

    def my_f(self, a, b):
        return a + b


class LoginModule(UIModule):
    def render(self, *args, **kwargs):
        print(self.request)
        print(self.request.uri)# uri = 路径 + 参数
        print(self.request.path)
        print(self.request.query)

        r = ''
        if self.request.query:
            r = '用户名或密码错误'

        return self.render_string('mymodules/login_module.html', result=r)


class BlogModule(UIModule):
    def render(self, *args, **kwargs):

        # dbutil = DBUtil()
        # UIModule无法直接找到Application对象
        # UIModule通过handler属性找到一个RequestHandler对象
        # 然后再通过该RequestHandler对象找到Application对象
        blogs = self.handler.application.dbutil.getblogs()
        return self.render_string('mymodules/blog_module.html',blogs=blogs)


class RegistHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('regist.html')

    def post(self, *args, **kwargs):
        name = self.get_body_argument('user', None)
        password = self.get_body_argument('pwd', None)
        city = self.get_body_argument('city', None)

        if name and password and city:
            avatar = None
            if self.request.files:
                file = self.request.files['avatar'][0]
                body = file['body']
                # 文件名由时间戳+本地名称拼接
                filename = str(time.time()) + file['filename']
                writer = open('mystatics/images/%s'%filename, 'wb')
                writer.write(body)
                writer.close()
                avatar = filename
            # 将原始的password利用摘要算法(md)进行格式的转换
            # md = hashlib.md5()
            # md.update(password.encode('utf8'))
            pwd = mymd5(password)

            # dbuitl = DBUtil()
            try:
                self.application.dbuitl.saveuser(name, pwd, avatar, city)
            except Exception as e:
                if avatar:
                    remove('mystatics/images/%s'%avatar)
                err = str(e) # 'duplicate','dberror'
                self.redirect('/regist?msg='+err)
            else:
                self.redirect('/')
        else:
            self.redirect('/regist?msg=empty')



class RegistModule(UIModule):
    def render(self, *args, **kwargs):
        #根据访问参数，提示不同的信息
        r = ''
        if self.request.query:
            err = self.request.query.split('=')[1]
            if err == 'empty':
                r = '请完整填写信息'
            if err == 'duplicate':
                r = '用户名已存在'
            if err == 'dberror':
                r = '数据库错误'

        return self.render_string('mymodules/regist_module.html', result=r)


app = MyApplication(hs=[('/', IndexHandler),
                            ('/login', LoginHandler),
                            ('/blog', BlogHandler),
                            ('/regist', RegistHandler)],
                  tp='mytemplates',
                  sp='mystatics',
                  um={'loginmodule': LoginModule,
                      'blogmodule': BlogModule,
                      'registmodule': RegistModule})
server = HTTPServer(app)
server.listen(8888)
IOLoop.current().start()
