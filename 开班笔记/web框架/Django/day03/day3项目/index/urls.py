from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^01_add/$', add_views),
    url(r'^02_query/$', query_views),
    url(r'^03_aulist/$', aulist_views),
    url(r'^04_delete/(\d+)/$', delete_views, name='del'),
    url(r'^05_upshow/(\d+)/$', upshow_views, name='up'),
    url(r'^06_upage/$', upage_views),
    url(r'^07_doQ/$', doQ_views),
    url(r'^08_raw/$', raw_views),
    url(r'^09_oto/$', oto_views),
    url(r'^10_otm/$', otm_views),
    url(r'^11_mtm/$', mtm_views),
    url(r'^12_mtm1/$',mtm1_views ),
    url(r'^12_obj/$', obj_views),
    url(r'^13_update/$', update_views, name='update'),

]