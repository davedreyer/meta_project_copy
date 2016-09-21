from django.shortcuts import render, redirect

def index(request):
	return render(request, 'disappearing_ninja/index.html')

def ninjas(request, color = None):

	if color == None:
		ninjas = ['disappearing_ninja/images/leonardo.jpg','disappearing_ninja/images/michelangelo.jpg','disappearing_ninja/images/raphael.jpg','disappearing_ninja/images/donatello.jpg']
		context = {'ninjas': ninjas}	

	elif color == 'blue':
		context = {'ninjas': ['disappearing_ninja/images/leonardo.jpg']}

	elif color == 'orange':
		context = {'ninjas': ['disappearing_ninja/images/michelangelo.jpg']}	
	
	elif color == 'red':
		context = {'ninjas': ['disappearing_ninja/images/raphael.jpg']}	

	elif color == 'purple':
		context = {'ninjas': ['disappearing_ninja/images/donatello.jpg']}		

	else: 
		context = {'ninjas': ['disappearing_ninja/images/notapril.jpg']}	

	return render(request, 'disappearing_ninja/ninjas.html', context)	
