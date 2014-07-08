from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User 
from django.template import RequestContext
from people.forms import RegistrationForm, LoginForm
from people.models import People
from django.contrib.auth import authenticate, login, logout

def PeopleRegistration(request):
	if request.user.is_authenticated():
		return redirect('/profile/')
		
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'], 
							email = form.cleaned_data['email'],
							password = form.cleaned_data['password'])
			user.save()
			people = People(user=user, name=form.cleaned_data['name'], birthday=form.cleaned_data['birthday'])
			people.save()
			return redirect('/profile/')
		else:
			return render_to_response('register.html', {'form': form}, 
						  context_instance=RequestContext(request))
        else:
        	''' user is not submitting the form, show the blank form '''
        	form = RegistrationForm()
        	context = {'form': form}
        	return render_to_response('register.html', context, context_instance=RequestContext(request))

@login_required
def Profile(request):     
	if not request.user.is_authenticated():
		return redirect('/login/')
	people = request.user.get_profile()
	context = {'people': people}
	return render_to_response('profile.html', context, context_instance=RequestContext(request))
	 
def LoginRequest(request):
	if request.user.is_authenticated():
		return redirect('/profile/')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			people = authenticate(username=username, password=password)
			if people is not None:
				login(request, people)
				return redirect('/profile/')
			else:
				return render_to_response('login.html', {'form': form},
						  context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form},
						  context_instance=RequestContext(request))
				
	else:
		''' user is not submitting the form, show the the login form '''
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context, context_instance=RequestContext(request))
def LogoutRequest(request):
	logout(request)
	return redirect('/')
	
        


