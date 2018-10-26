from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', login, name='login'),
    url(r'^loginIn/$', login_in, name='loginIn'),
    url(r'^register/$', register, name='register'),
    url(r'^registerIn/$', register_in, name='registerIn'),
]
