 from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import * 
from .models import *

# Create your views here.
def request_views(request):
    # print(dir(request))
    # return HttpResponse('ok')

    scheme = request.scheme
    body = request.body
    host = request.get_host()
    path = request.path
    method = request.method
    get = request.GET
    post = request.POST
    cookies = request.COOKIES

    return render(request, '01_request.html', locals())


def login_views(request):
    if request.method == 'GET':
        return render(request, '02_login.html')
    else:
        uname = request.POST['uname']
        upwd = request.POST['upwd']
        return HttpResponse(uname+''+upwd)


def get_views(request):
    uname = request.GET.get('uname', '')
    upwd = request.GET.get('upwd', '')
    if uname and upwd:
        return HttpResponse(uname+' '+upwd)
    else:
        return render(request, '03_login.html')


def query_views(request):
    id = request.GET.get('id', '')
    name = request.GET.get('name', '')

    return HttpResponse(id+''+name)


def form_views(request):
    if request.method == 'GET':
        form = RemarkForm()
        return render(request, '04_form.html', locals())
    else:
        #1.将request.POST的数据交给RemarkForm()
        form = RemarkForm(request.POST)

        #2.验证数据是否都符合规范（必须要通过验证）
        if form.is_valid():
            #3.通过验证后，再通过cleaned_data取值
            cd = form.cleaned_data
            return HttpResponse(cd['email'])


def register_views(request):
    if request.method == 'GET':
        form = RegisterForm()
        return render(request, '05_register.html', locals())
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            users = Users(**cd)
            users.save()
            return HttpResponse('ok')


def modelForm_views(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, '06_login.html',locals())


def addCookie_views(request):
    # resp = HttpResponse('添加cookie成功')
    # resp.set_cookie('uanme1', 'zsf', 60*60*24)
    # return resp

    # 使用模板
    # resp = render(request, '07_setcookie.html', locals())
    # resp.set_cookie('uname2', 'zhang', 60*60*24*31)
    # return resp

    # 使用重定向
    resp = HttpResponseRedirect('/02_login/')
    resp.set_cookie('uname3', 'li', 60*60*24*365)
    return resp


def getCookie_views(request):
    cookies = request.COOKIES
    print(cookies)
    return HttpResponse('get cookies ok')


def setSession_views(request):
    uname = '张三丰'
    uemail = 'zsf@163.com'
    #将以上两个数据保存进session
    request.session['uname'] = uname
    request.session['uemail'] = uemail
    return HttpResponse('add session ok')


def getSession_views(request):
    uname = request.session.get('uname')
    uemail = request.session.get('uemail')
    return HttpResponse(uname+':'+uemail)
