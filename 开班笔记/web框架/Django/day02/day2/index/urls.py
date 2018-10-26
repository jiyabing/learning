from django.conf.urls import url
from .views import *

#当访问路径是http://localhost:8000/index/****
#则交给当前的urls.py去处理
urlpatterns = [
	#匹配访问路径是index的话，则交给index_views去处理
	#http://localhost:8000/index/index
	url(r'^$', index_views),
	url(r'^login$', login_views),
]