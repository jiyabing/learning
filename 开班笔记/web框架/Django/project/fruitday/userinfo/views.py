from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
import logging
from .models import *
from django.db import DatabaseError


# Create your views here.


def register_in(request):
    return render(request, 'register.html')


def register_(request):
    # 获取注册信息
    # 判断用户是否存在
    # 注册用户
    # 返回页面
    if request.method == 'GET':
        return redirect('/user/register')
    else:
        user = request.POST['user_name']
        users = UserInfo.objects.filter(uname=user)
        if users:
            msg = '用户名已存在'
            return render(request, 'register.html', locals())
        else:
            password = request.POST['user_pwd']
            cpassword = request.POST['user_cpwd']
            if password != cpassword:
                msg = '两次密码不一致'
                return render(request, 'register.html', locals())
            else:
                pwd = make_password(password, 'abc', 'pbkdf2_sha1')
                email = request.POST['email']
                phone = request.POST['phone']
                try:
                    UserInfo.objects.create(uname=user, upassword=pwd, email=email, phone=phone)
                except DatabaseError as e:
                    logging.warning(e)
                return render(request, 'index.html')


def login_in(request):
    return render(request, 'login.html')


def login_(request):
    if request.method == 'POST':
        user = UserInfo()
        user.uname = request.POST['user_name']
        user.upassword = request.POST['user_pwd']
        try:
            users = UserInfo.objects.filter(uname=user.uname)
            print(users)
            if len(users) <= 0:
                msg = '用户不存在'
                return render(request, 'login.html', locals())
            if not check_password(user.upassword, users[0].upassword):
                msg = '密码错误'
                return render(request, 'login.html', locals())
        except DatabaseError as e:
            logging.warning(e)

        request.session['user_id'] = users[0].id
        request.session['user_name'] = users[0].uname
        # return render(request, 'index.html')
        return redirect('/')
    else:
        return redirect('/user/login')


def login_out(request):
    try:
        if request.session['user_name']:
            del request.session['user_name']
            del request.session['user_id']
    except KeyError as e:
        logging.warning(e)
    return redirect('/')


def add_ads(request):
    # 获取用户（session中获取）
    # 获取前端页面传来的信息（收件人姓名，地址，电话）
    # 对数据库进行增加操作
    # 返回页面
    pass


def user_ads(request):
    # 获取用户id（session中获取）
    # 查询数据库中Address表中该用户id的数据
    # 返回页面
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    content = {'adss':adss}
    return render(request, '', content)


def delete_ads(request):
    # 获取用户id
    # 获取地址id
    # 查询该数据
    # 删除该数据
    # 返回页面
    user_id = request.session.get('user_id')
    adsid = request.GET.get('adsid')
    try:
        delads = Address.objects.get(id=adsid, user_id=user_id)
        delads.delete()
    except DatabaseError as e:
        logging.warning(e)
    return redirect('')