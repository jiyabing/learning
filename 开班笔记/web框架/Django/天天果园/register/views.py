from django.shortcuts import render
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

# Create your views here.

def register_views(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        #接收用户手机号，判断号码是否存在
        user = request.POST['user']
        users = Users.objects.filter(uphone=user)
        if users:
            #手机号已注册过，给出提示，回到注册页面
            errMsg = '手机号已注册'
            return render(request, 'register.html',locals())
        else:
            pwd = request.POST['pwd']
            name = request.POST['uname']
            email = request.POST['email']
            Users.objects.create(uphone=user, upwd=pwd, uname=name, uemail=email)
            return HttpResponseRedirect('/')
