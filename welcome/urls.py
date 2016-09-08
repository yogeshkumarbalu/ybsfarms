from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^products/$', views.products, name='products'),
	url(r'^animals/$', views.animals, name='animals'),
	url(r'^culture/$', views.culture, name='culture'),
	url(r'^bulls/$', views.bulls, name='bulls'),
	url(r'^trees/$', views.trees, name='trees'),
	url(r'^plants/$', views.plants, name='plants'),
	url(r'^flowers/$', views.flowers, name='flowers'),
	url(r'^fertilizers/$', views.fertilizers, name='fertilizers'),
	url(r'^lectures/$', views.lectures, name='lectures'),
	url(r'.*', views.home, name='home'),
]
