from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', index_views)
]# + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)