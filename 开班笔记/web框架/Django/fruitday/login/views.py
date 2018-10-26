from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def login_views(request):
    if request.method == "GET":
        #判断cookies中是否有id 和 手机号码
        if 'id' in request.COOKIES and 'phone' in request.COOKIES:
            return HttpResponse('欢迎'+request.COOKIES['phone']+'回来')
        else:
            form = LoginForm()
            return render(request, 'login.html', locals())
    else:
        uphone = request.POST['user']
        upwd = request.POST['pwd']
        users = Users.objects.filter(手机号码=uphone, 用户密码=upwd)
        if users:
            resp = HttpResponse('登录成功')
            #是否记住密码
            if 'isSave' in request.POST:
                MAX_AGE = 60*60*60*366
                resp.set_cookie('id', users[0].id, MAX_AGE)
                resp.set_cookie('phone', users[0].手机号码, MAX_AGE)
            return resp
        else:
            form = LoginForm()
            return render(request, 'login.html', locals())


def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        #接收用户手机号，判断号码是否存在
        user = request.POST['user']
        users = Users.objects.filter(手机号码=user)
        if users:
            #手机号已注册过，给出提示，回到注册页面
            errMsg = '手机号已注册'
            return render(request, 'register.html',locals())
        else:
            pwd = request.POST['pwd']
            name = request.POST['uname']
            email = request.POST['email']
            Users.objects.create(手机号码=user, 用户密码=pwd, 用户昵称=name, 电子邮箱=email)
            return HttpResponse('ok')
