from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^survey/process$', views.process, name="views"),
	url(r'^result$', views.result, name="result")
]