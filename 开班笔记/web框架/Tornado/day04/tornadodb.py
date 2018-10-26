import hashlib
import json, pymysql, time
from os import remove

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, UIModule

from Tornado部分.day04.util.myutil import mymd5


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
        '''
        if name == 'abc' and password == '123':
            # 如果用户真上传了文件，则把上传的文件保存到服务器
            # self.request是RequestHandler的一个属性，引用HttpServerRequest对象，该对象中封装了与请求相关的所有内容
            print(self.request)
            # HttpServerRequest对象的files属性引用着用户通过表单上传的文件
            # 如果用户没有上传文件，files属性是空字典{}
            # 如果上传了文件，则files返回的对象是如下：
            # {'avatar':[
            # {'content_type':'image/jpeg', 'body': 二进制格式表示的图像的内容, 'filename': '上传者本地图像名称'},
            # {},
            # {}...]}
            print(self.request.files)
            if self.request.files:
                avs = self.request.files['avatar']
                for a in avs:
                    body = a['body']
                    # 上传的这一个文件内容保存到服务器的硬盘上
                    writer = open('upload/'+a['filename'], 'wb')
                    writer.write(body)
                    writer.close()


            # 跳转页面
            self.redirect('/blog?user='+name)
        else:
            self.redirect('/?msg=用户信息不正确')
        '''
        # 1.通过pymysql建立与数据库的连接
        settings = {'host': '127.0.0.1',
                    'port': 3306,
                    'user': 'root',
                    'password': '123456',
                    'database': 'blog_db',
                    'charset': 'utf8'}
        connection = pymysql.connect(**settings)

        # 2.通过连接获取游标
        cursor = connection.cursor()

        # 3.利用游标发送SQL语句
        # 以下sql语句可能会被注入攻击
        # sql = 'select count(*) from tb_user ' \
        #       'where user_name="%s" and user_password="%s"' % (name, password)

        # 以下sql语句可以防止注入攻击
        sql = 'select count(*) from tb_user ' \
              'where user_name=%s and user_password=%s'
        pwd = mymd5(password)
        params = (name, pwd)

        cursor.execute(sql, params)

        # 4.如果有需要，利用cursor获取数据库结果
        # result = cursor.fetchall()  # ((1,),)
        result = cursor.fetchone()  # (0,)
        print(result)
        if result[0]:
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
        return self.render_string('mymodules/blog_module.html',blogs=[{
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

            settings = {'host': '127.0.0.1',
                        'port': 3306,
                        'user': 'root',
                        'password': '123456',
                        'database': 'blog_db',
                        'charset': 'utf8'}
            connection = pymysql.connect(**settings)
            cursor = connection.cursor()
            sql = 'insert into tb_user(user_name, user_password, user_avatar, user_city) ' \
                  'values(%s,%s,%s,%s)'
            # 将原始的password利用摘要算法(md)进行格式的转换
            # md = hashlib.md5()
            # md.update(password.encode('utf8'))
            pwd = mymd5(password)
            params = (name, pwd, avatar, city)
            try:
                cursor.execute(sql, params)
                # 提交
                cursor.connection.commit()
            except Exception as e:
                if avatar:
                    remove('mystatics/images/%s'%avatar)
                err = str(e)
                code = err.split(',')[0].split('(')[1]
                if code == '1062':
                    r = 'duplicate'
                else:
                    r = 'dberror'
                self.redirect('/regist?msg='+r)
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


app = Application(handlers=[('/', IndexHandler),
                            ('/login', LoginHandler),
                            ('/blog', BlogHandler),
                            ('/regist', RegistHandler)],
                  template_path='mytemplates',
                  static_path='mystatics',
                  ui_modules={'loginmodule': LoginModule,
                              'blogmodule': BlogModule,
                              'registmodule': RegistModule})
server = HTTPServer(app)
server.listen(8888)
IOLoop.current().start()
