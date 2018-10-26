import logging

from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ObjectDoesNotExist
from django.db import DatabaseError
from django.shortcuts import render, redirect
from userinfo.models import UserInfo
# Create your views here.

auth_check = 'abc'


def login(request):
    return render(request, 'login.html')


def login_in(request):
    if request.method == 'POST':
        user = UserInfo()
        user.name = request.POST.get('user')
        user.password = request.POST.get('pwd')
        try:
            find_user = UserInfo.objects.filter(name=user.name)
            if len(find_user) <= 0:
                messages.add_message(request, messages.ERROR, '该用户未注册')
                return redirect('/user/login')
            if not check_password(user.password, find_user[0].password):
                return render(request, 'login.html',
                              {'user_info': user, 'message_error': '密码错误'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        return redirect('/')
    return redirect('user/login')


def register(request):
    return render(request, 'register.html')


def register_in(request):
    if request.method == 'POST':
        new_user = UserInfo()
        new_user.name = request.POST.get('user')
        if not new_user.name:
            return render(request, 'register.html', {'message0': '请输入用户名'})
        try:
            a = UserInfo.objects.get(name=new_user.name)
            if a:
                return render(request, 'register.html', {'message1': '该用户已注册'})
        except ObjectDoesNotExist as e:
            logging.warning(e)
        if request.POST.get('pwd') != request.POST.get('cpwd'):
            return render(request, 'register.html', {'message2': '两次密码不一致'})
        new_user.password = make_password(request.POST.get('pwd'), auth_check, 'pbkdf2_sha1')
        new_user.phone = request.POST.get('phone')
        new_user.email = request.POST.get('email')
        try:
            new_user.save()
        except DatabaseError as e:
            logging.warning(e)
        return render(request, 'index.html')
    return render(request, 'register.html')