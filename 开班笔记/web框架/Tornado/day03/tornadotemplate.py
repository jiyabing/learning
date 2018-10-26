import json

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler, UIModule


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


class BlogHandler(RequestHandler):
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
        pass


app = Application(handlers=[('/', IndexHandler),
                            ('/login', LoginHandler),
                            ('/blog', BlogHandler),
                            ('/regist', RegistHandler)],
                  template_path='mytemplates',
                  static_path='mystatics',
                  ui_modules={'loginmodule': LoginModule,
                              'blogmodule': BlogModule})
server = HTTPServer(app)
server.listen(8888)
IOLoop.current().start()
