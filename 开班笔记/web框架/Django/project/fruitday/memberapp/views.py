import random

from django.shortcuts import render, get_object_or_404
from .models import *
from django.db import DatabaseError
import logging

# Create your views here.


def index(request):
    # 方法一：
    # 查询数据库的全部分类全部商品
    # 按照分类名查询商品，并分别储存传回前端
    try:
        good_fruit_type = get_object_or_404(GoodsType, title='水果')
        fruit_goods = random.sample(list(good_fruit_type.goods_set.all()), 2)
    except DatabaseError as e:
        logging.warning(e)

    # 方法二：
    # 查询全部分类
    # 查询全部商品
    types = GoodsType.objects.all()
    goods = Goods.objects.all()

    # 方法三：
    # 查询分类
    # 查询该类下的全部商品
    ac = []
    typess = GoodsType.objects.all()
    # print(typess)
    for type in typess:
        b = {}
        b['type'] = type.title
        good_type = get_object_or_404(GoodsType, title=type.title)
        f_goods = random.sample(list(good_type.goods_set.all()), 2)
        b['goods'] = f_goods
        ac.append(b)
    # print(ac)

    return render(request, 'index.html', {'good_list': locals()})


def detail_one(request):
    # 查询数据库该id的商品
    good_id = request.GET.get('goodid')[:-1]
    try:
        goodone = Goods.objects.filter(id=good_id)
    except DatabaseError as e:
        logging.warning(e)
    return render(request, 'detail.html', {'goodone': goodone[0]})