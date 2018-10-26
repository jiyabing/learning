from django.conf.urls import url
from goods.views import index_view, detail_view, list_view

urlpatterns = [
    url(r'^$', index_view, name='index'),  # 首页
    url(r'^goods/(?P<sku_id>\d+)$', detail_view, name='detail'),  # 详情页
    url(r'^list/(?P<type_id>\d+)/(?P<page>\d+)$', list_view, name='list'),  # 列表页
]
