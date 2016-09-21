from django.shortcuts import render, redirect
import random
import datetime
from django.core.urlresolvers import reverse

def index(request):
	if 'gold' not in request.session:
		request.session['gold'] = 0
		request.session['log'] = []
	return render(request, 'ninja_gold/index.html')

def process_money(request):

	if request.POST['building'] == 'farm':
	    random_gold = random.randrange(10, 21)
	    description = 'Earned {} golds from the farm! ({})'.format(random_gold, datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
	    request.session['gold'] += random_gold 
	    request.session['log'].append(description)  

	elif request.POST['building'] == 'cave':
		random_gold = random.randrange(5, 11)
		description = 'Earned {} golds from the cave! ({})'.format(random_gold, datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
		request.session['gold'] += random_gold 
		request.session['log'].append(description)
	    
	elif request.POST['building'] == 'house':
		random_gold = random.randrange(2, 6)
		description = 'Earned {} golds from the house! ({})'.format(random_gold, datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
		request.session['gold'] += random_gold 
		request.session['log'].append(description)

	else:
		random_gold = random.randrange(-50, 51)
		if random_gold < 0:
			description = 'Lost {} golds from the casino! ({})'.format(random_gold, datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
			request.session['gold'] -= random_gold
			request.session['log'].append(description) 
		else:
			description = 'Won {} golds from the casino! ({})'.format(random_gold, datetime.datetime.now().strftime('%Y-%m-%d %I:%M:%S %p'))
			request.session['gold'] += random_gold
			request.session['log'].append(description)	
	return redirect(reverse('gold:index'))
