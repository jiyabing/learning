from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index_views(request):
	return HttpResponse('这是news应用中的index视图')

def template_views(request):
    #1.通过loader加载模板
    t = loader.get_template('01_template.html')

    #2.将模板渲染成字符串
    html = t.render()

    #3.将字符串通过HttpResponse进行响应
    return HttpResponse(html)

def render_views(request):
    return render(request, '01_template.html')

def var1_views(request):
    l = ['老舍', '朱自清',]
    t = ('三国', '水浒')
    d = {'一': 1, '二': 2}

    dic = {
        'num': 1001,
        'str': 'Hello World',
        'list': l,
        'tuple': t,
        'dict': d,
        'func': func(10, 20),
        'Dog': Dogs(),
    }

    t = loader.get_template('02_var.html')
    html = t.render(dic)
    return HttpResponse(html)

def var2_views(request):
    l = ['老舍', '朱自清',]
    t = ('三国', '水浒')
    d = {'一': 1, '二': 2}

    dic = {
        'num': 1001,
        'str': 'Hello World',
        'list': l,
        'tuple': t,
        'dict': d,
        'func': func(10, 20),
        'Dog': Dogs(),
    }
    return render(request, '02_var.html', dic)

def var3_views(request):
    book = '项链'
    author = '莫泊桑'
    #dic = {'book': '《背影》', 'author': '朱自清'}
    #return render(request, '03_var.html', dic)
    return render(request, '03_var.html', locals())

def tag_views(request):
    l = ['zhang', 'li', 'wang']
    return render(request, '04_tag.html', locals())

def parent_views(request):
    return render(request, '06_parent.html')

def chile_views(request):
    return render(request, '07_child.html')


def func(a, b):
    return a + b

class Dogs(object):
    dog = "二哈"
    def fun(self):
        return "喜欢拆家"