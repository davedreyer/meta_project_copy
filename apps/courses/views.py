from django.shortcuts import render, redirect

from .models import Course
from django.core.urlresolvers import reverse
from models import Course, User

def index(request):
	context = {
		"courses": Course.objects.all().order_by('-created_at'),
	}
	return render(request, 'courses/index.html', context)

def create_course(request):
	if request.method=="POST":
		Course.objects.create(name=request.POST["name"], description=request.POST["description"])
	return redirect(reverse('courses:index'))

def delete_course(request, course_id):
	if request.method=="GET":
		context = {
		"course": Course.objects.get(id=course_id),
		}
		return render(request, 'courses/delete.html', context)

	elif request.method=="POST":
		Course.objects.get(id=course_id).delete()
		return redirect(reverse('courses:index'))

def users_courses(request):
	if request.method=="GET":

		context = {
			"courses": Course.objects.all().order_by('id'),
			"users": User.objects.all()
		}

		return render(request, 'courses/users_courses.html', context)

	if request.method=="POST":	
	
		user = User.objects.get(id=request.POST['user'])
		course = Course.objects.get(id=request.POST['course'])
		course.courselinks.add(user)
		course.save()
				
		return redirect(reverse('courses:users_courses'))
		







		

