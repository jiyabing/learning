from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F, Q

# Create your views here.
def add_views(request):
    
    #方式一
    Author.objects.create(name='天蚕土豆', age=30)

    #方式二
    obj = Author(name='唐门三少', age=35)
    obj.save()

    #方式三
    dic = {
        'name':'徐虹',
        'age':37,
        'email':'xuhong@163.com',
    }
    obj = Author(**dic)
    obj.save()
    

    '''
    Book.objects.create(title='武动乾坤', publicate_date='2010-08-09')
    Book(title='诛仙', publicate_date='2008-7-7').save()
    Book(**{'title':'盘龙', 'publicate_date':'2009-08-08'}).save()
    '''

    return HttpResponse('添加成功!')


def query_views(request):
    '''
    #所有查询
    auList = Author.objects.all()
    print(auList)
    for au in auList:
        print('{} {} {}'.format(au.name, au.age, au.email))

    
    #查询相应的列
    auDict = Author.objects.values('name', 'age')
    print(auDict)
    for au in auDict:
        print(au['name'],au['age'])
    '''

    #查询排序
    # auList1 = Author.objects.order_by('-age')
    # print(auList1)
    # for au in auList1:
    #     print(au.id, au.name, au.age)

    #对条件取反：exclude(条件)
    # auList = Author.objects.exclude(age=30)
    # for au in auList:
    #     print(au.id, au.name, au.age)

    #查询name属性值包含'土豆'的所有记录
    auList = Author.objects.filter(name__contains='土豆')
    print(auList)
    for au in auList:
        print(au.id, au.name, au.age)

    return HttpResponse('查询成功!')


def aulist_views(request):
    #aulist = Author.objects.all()
    aulist = Author.objects.filter(isActive=True)
    return render(request, '01_aulist.html', locals())

def delete_views(request, num):
    # Author.objects.get(id=num).delete()

    #以修改数据isActive状态值的方式来表示删除数据
    au = Author.objects.get(id=num)
    au.isActive = False
    au.save()
    
    #转发
    #return aulist_views(request)

    #重定向
    return HttpResponseRedirect('/index/03_aulist/')


def upshow_views(request, num):
    au = Author.objects.get(id=num)
    return render(request, '02_update.html', locals())


def upage_views(request):
    #修改所有人的年龄加10
    Author.objects.all().update(age=F('age')+10)
    return HttpResponseRedirect('/index/03_aulist/')


def doQ_views(request):
    aulist = Author.objects.filter(Q(id=5)|Q(age__gt=45))
    return render(request, '01_aulist.html', locals())


def raw_views(request):
    sql = 'select * from index_author where email is not null'
    aulist = Author.objects.raw(sql)
    for au in aulist:
        print(au.name, au.age)
    return HttpResponse('查询成功！')


def oto_views(request):
    '''
    #正向查询：通过wife 找 author
    #1.获取id为1的wife信息
    wife = Wife.objects.get(id=1)
    #2.再获取wife对应的Author
    author = wife.author
    '''

    #反向查询：通过author 找 wife
    author = Author.objects.get(id=7)
    wife = author.wife

    return render(request, '03_oto.html', locals())


def otm_views(request):
    '''
    #正向查询
    book = Book.objects.get(id=1)
    publisher = book.publisher
    '''

    #反向查询
    #1.查询id为1的出版社信息
    publisher = Publisher.objects.get(id=1)
    #2.查询该出版社关联的所有图书
    books = publisher.book_set.all()
    
    return render(request, '04_otm.html', locals())


def mtm_views(request):
    #正向查询，通过Author查询book
    author = Author.objects.get(id=5)
    books = author.book.all()

    #反向查询，通过Book查询author
    book = Book.objects.get(id=1)
    authors = book.author_set.all()

    return render(request, '05_mtm.html', locals())


def mtm1_views(request):
    #正向查询，Author ---> publisher
    author = Author.objects.get(name='唐门三少')
    publishers = author.publisher.all()

    #反向查询，Publisher ---> author
    publisher = Publisher.objects.get(name='武汉大学出版社')
    authors = publisher.author_set.all()

    return render(request, '06_mtm.html', locals())


def obj_views(request):
    count = Author.objects.auCount()
    aulist = Author.objects.lt_age(50)
    for au in aulist:
        print(au.name, au.age)

    books = Book.objects.titleContains('斗') 
    for book in books:
        print(book.title)
    return HttpResponse('查询成功')


def update_views(request):
    id = request.POST['id']
    name = request.POST['name']
    age = request.POST['age']
    email = request.POST['email']

    au = Author.objects.get(id=id)
    au.name = name
    au.age = age
    au.email = email
    au.save()
    return HttpResponseRedirect('/index/03_aulist/')