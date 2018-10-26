from django.conf.urls import url
from django.contrib import admin
from userinfo import views

urlpatterns = [
    url(r'^register/', views.register_in, name='register'),
    url(r'^registerin/', views.register_, name='register_in'),
    url(r'^login/', views.login_in, name='login'),
    url(r'^loginin/', views.login_, name='login_in'),
    url(r'^loginut/', views.login_out, name='login_out'),
]
