import datetime

from django.shortcuts import render

from userinfo.models import Address
from .models import *
from userinfo import *
from memberapp import *
from django.db import DatabaseError
import logging
import json
from django.http import HttpResponse

# Create your views here.


def add_cart(request):
    # 声明一个新的购物车
    new_cart = CartInfo()
    # 获取前端数据(商品id，商品数量)
    good_id = request.GET.get('goodid')
    good_count = request.GET.get('goodcount')
    # 获取用户id
    user_id = request.session.get('user_id')
    # print(good_id, good_count, user_id)
    # 查询用户
    user_ = UserInfo.objects.get(id=user_id)
    # 查询商品
    good_ = Goods.objects.filter(id=good_id)
    print(good_[0])
    # 判断商品是否存在
    if len(good_) > 0:
        new_cart.user = user_
        new_cart.good = good_[0]
    else:
        content = {'static': 'ok', 'text': '无该商品'}
        return HttpResponse(json.dumps(content))
        # return render(request, 'index.html')
    # 查询购物车中该用户是否有此商品，商品数量转换成int，如果有加上相应数量商品，没有直接保存
    new_cart.ccount = int(good_count)
    try:
        old_good = CartInfo.objects.filter(user_id=user_id, good_id=good_id)
        if len(old_good) > 0:
            old_good[0].ccount = old_good[0].ccount + new_cart.ccount
            old_good[0].save()
        else:
            new_cart.save()
    except DatabaseError as e:
        logging.warning(e)
    # 返回页面
    content = {'static': 'ok', 'text': '添加成功'}
    return HttpResponse(json.dumps(content))
    # return render(request, 'index.html')


def delete_cart(request):
    user_id = request.session.get('user_id')
    cart_id = request.GET.get('cart_id')
    try:
        delcart = CartInfo.objects.filter(user_id=user_id, id=cart_id)
        delcart.delete()
    except DatabaseError as e:
        logging.warning(e)
    content = {'static': 'ok', 'msg': '删除成功'}
    return HttpResponse(json.dumps(content))


def cart_info(request):
    user_id = request.session.get('user_id')
    find_goods = CartInfo.objects.filter(user_id=user_id)
    return render(request, 'cart.html', {'find_goods': find_goods})


def order(request):
    user_id = request.session.get('user_id')
    adss = Address.objects.filter(user_id=user_id)
    content = {'adss':adss}
    return render(request, 'order.html', content)


def add_order(request):
    # 获取数据
    # 存数据
    # 返回结果
    user_id = request.session.get('user_id')
    orderdetail = request.POST.get('acot')
    adsname = request.POST.get('adsname')
    adsphone = request.POST.get('adsphone')
    ads = request.POST.get('ads')
    acot = 2
    acount = 99.99
    orderNo = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    try:
        user = UserInfo.objects.get(id=user_id)
        order = Order.objects.create(orderNo=orderNo, orderdetail=orderdetail, adsname=adsname,
                                     adsphone=adsphone, ads=ads, user=user, acot=acot, acount=acount)
    except DatabaseError as e:
        logging.warning(e)
    content = {'static': 'ok'}
    return HttpResponse(json.dumps(content))



