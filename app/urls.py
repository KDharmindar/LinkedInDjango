from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, {'next_page': '/'}, name='logout'),
    url(r'^pinverify/$', views.pinverify, name='pinverify'),
    url(r'^account/$', views.account, name='account'),
    url(r'^register/$', views.register, name='register'),
]
