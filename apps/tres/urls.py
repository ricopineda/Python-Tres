from django.conf.urls import url
from . import views           
urlpatterns = [
	url(r'^$', views.index),
	url(r'^register$', views.register),
	url(r'^login$', views.login),
	url(r'^logout$', views.logout),
	url(r'^home$', views.home),
	url(r'^add$', views.add),
	url(r'^add_trip$', views.add_trip),
	url(r'^destination/(?P<id>\d+)$', views.destination),
	url(r'^join/(?P<id>\d+)$', views.join),

]