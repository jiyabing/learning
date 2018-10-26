from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, RequestHandler


class IndexHandler(RequestHandler):
    def get(self, *args, **kwargs):
        html = "<form action='/login' method='post' enctype=multipart/form-data>"\
               "<span>用户名: <span><input type='text' name='user' placeholder='用户名'><br>"\
               "<span>密码: <span><input type='password' name='pwd' placeholder='密码'><br>"\
               "<input type=file name=avatar><br>" \
               "<input type=file name=avatar><br>"\
               "<input type='submit' value='登录'>    "\
               "<input type='reset' value='重置'>"\
               "</form>"

        fail_html = "<form action='/login' method='post'>" \
                    "<span>用户名: <span><input type='text' name='user' placeholder='用户名'><br>" \
                    "<span>密码: <span><input type='password' name='pwd' placeholder='密码'><br>" \
                    "<span style=color:red;>用户名或密码错误</span><br>"\
                    "<input type='submit' value='登录'>    " \
                    "<input type='reset' value='重置'>" \
                    "</form>"

        msg = self.get_query_argument('msg', None)
        if msg:
            self.write(fail_html)
        else:
            self.write(html)

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
    def get(self, *args, **kwargs):
        name = self.get_query_argument('user', None)
        if name:
            self.write('欢迎'+name+'使用')
        else:
            self.redirect('欢迎使用')

    def post(self, *args, **kwargs):
        pass


app = Application(handlers=[('/', IndexHandler),
                            ('/login', LoginHandler),
                            ('/blog', BlogHandler)
                            ])
server = HTTPServer(app)
server.listen(8888)
IOLoop.current().start()
