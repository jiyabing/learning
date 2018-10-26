from django.conf.urls import url
from .views import *

#当访问路径是http://localhost:8000/news/****
#则交给当前的urls.py去处理
urlpatterns = [
	#匹配访问路径是index的话，则交给index_views去处理
	#http://localhost:8000/news/index
	#http://localhost:8000/news/
	url(r'^$', index_views),

    #http://localhost:8000/news/01_template/
    url(r'^01_template/$', template_views),

    #http://localhost:8000/news/02_render/
    url(r'^02_render/$', render_views),

    #http://localhost:8000/news/03_variable/
    url(r'^03_variable/$', var1_views),

    #http://localhost:8000/news/04_variable/
    url(r'^04_variable/$', var2_views),

    #http://localhost:8000/news/05_exer/
    url(r'^05_exer/$', var3_views),

    #http://localhost:8000/news/06_tag/
    url(r'^06_tag/$', tag_views),

    #http://localhost:8000/news/08_parnet
    url(r'08_parent/$', parent_views),

    #http://localhost:8000/news/09_child
    url(r'09_child/$', chile_views),


]