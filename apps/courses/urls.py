from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name = "index"),
	url(r'^course/create$', views.create_course, name="create"),
	url(r'^course/delete/(?P<course_id>[0-9]+)$', views.delete_course, name="delete"),
	url(r'^course/users_courses$', views.users_courses, name="users_courses")
]