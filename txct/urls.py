from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.text_list, name='text_list'),
    url(r'^text/(?P<pk>\d+)/$', views.text_detail, name='text_detail'),
    url(r'^cinc/$', views.text_5, name='cinc'),
    url(r'^deu/$', views.text_10, name='deu'),
    url(r'^quinze/$', views.text_15, name='quinze'),
    url(r'^vint/$', views.text_20, name='vint'),
    url(r'^vinticinc/$', views.text_25, name='vinticinc'),
]
