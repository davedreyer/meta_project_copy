from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^ninjas/$', views.ninjas, name="views"),
	url(r'^ninjas/(?P<color>\w+)$', views.ninjas, name="colors")
]