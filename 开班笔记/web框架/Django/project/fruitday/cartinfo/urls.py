from django.conf.urls import url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^addcart', add_cart, name='add_cart'),
    url(r'^cart', cart_info, name='cart'),
    url(r'^order', order, name='order'),
    url(r'^addorder', add_order, name='addorder'),
]