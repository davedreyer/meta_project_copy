from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.core.urlresolvers import reverse

def index(request):
	if request.method=="GET":
		query = User.objects.all()[0]
		links_query = query.courselinks.all()
		context = {
			'query': links_query
		}
		return render(request, 'user_reg/index.html', context)

	if request.method=="POST":
		if request.POST['process'] == 'registration':
			check = User.objects.reg_check(request.POST)
			if check['created']:
				messages.success(request, "Success! Welcome {}!".format(check['new_user'].first_name))	
				return redirect(reverse('user:success'))	
			else:
				for x in check['errors']:
					messages.error(request, x)
				return redirect(reverse('user:index'))	
		
		elif request.POST['process'] == 'login':
			check = User.objects.login_check(request.POST)
			if check['login'] == True:
				messages.success(request, "Hi {}! You successfully logged in!".format(check['user'].first_name))
				return redirect(reverse('user:success'))
			else:
				for x in check['errors']:
					messages.error(request, x)
				return redirect(reverse('user:index'))		

def success(request):
	if request.method=="GET":
		return render(request, 'user_reg/success.html')					
