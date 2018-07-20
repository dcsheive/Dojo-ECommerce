from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.adminmain, name='adminmain'),
    url(r'^login$', views.adminlogin, name='adminlogin'),
    url(r'^orders$', views.adminorders, name='adminorders'),
    url(r'^products$', views.adminproducts, name='adminproducts'),
    url(r'^logout$', views.adminlogout, name='adminlogout'),
    url(r'^product/(?P<id>\d+)$', views.adminprod, name='adminprod'),
    url(r'^addprod$', views.addprod, name='addprod'),
    url(r'^delete/(?P<id>\d+)$', views.deleteprod, name='admindelete')
]