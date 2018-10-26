from django.conf.urls import url
from user.views import login_view, register_view, active_view, logout_view
from user.views import UserInfoView, UserOrderView, AddressView

urlpatterns = [
    url(r'^register/$', register_view, name='register'),  # 注册
    url(r'^active/$', active_view, name='active'),  # 激活
    url(r'^login/$', login_view, name='login'),  # 登录
    url(r'^logout$', logout_view, name='logout'),  # 退出
    url(r'^$', UserInfoView.as_view(), name='user'),  # 用户中心-信息页
    url(r'^order/(?P<page>(\d)*)$', UserOrderView.as_view(), name='order'),  # 用户中心-订单页
    url(r'^address$', AddressView.as_view(), name='address'),  # 用户中心-地址页
]
