from django.conf.urls import url
from assets import views


urlpatterns = [
    url(r'^report/', views.report, name='report'),
]