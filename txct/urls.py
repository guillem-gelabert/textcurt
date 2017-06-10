from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.text_list, name='text_list'),
    url(r'^text/(?P<pk>\d+)/$', views.text_detail, name='text_detail'),
]
