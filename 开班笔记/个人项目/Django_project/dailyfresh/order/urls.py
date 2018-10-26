from django.conf.urls import url
from order.views import *

urlpatterns = [
    url(r'^place$', order_place_view, name='place'), # 提交订单页面
    url(r'^commit$', order_commit_view, name='commit'), # 创建订单
    url(r'^pay$', order_pay_view, name='pay'), # 订单支付
    url(r'^check$', order_check_view, name='check'), # 订单交易结果
    url(r'^comment/(?P<order_id>.*)$', comment_view, name='comment'), # 订单评论
]