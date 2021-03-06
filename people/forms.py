from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from people.models import People

class RegistrationForm(ModelForm):
	username = forms.CharField(label=(u'User Name'))
	email = forms.EmailField(label=(u'Email Address'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
	passwordverify = forms.CharField(label=(u'Verify Password'), widget=forms.PasswordInput(render_value=False))
	
	class Meta:
		model = People
		exclude = ('user',)
		
	def clean_username(self):
		username = self.cleaned_data['username']
		try: 
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('That username is already taken, please take another.')
		
	def clean(self):
		password = self.cleaned_data.get('password', None)
		passwordverify = self.cleaned_data.get('passwordverify', None)
		if password and passwordverify and password != passwordverify:
			raise forms.ValidationError("Your passwords did not match, please try again!")
		return self.cleaned_data

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User Name'))
	password = forms.CharField(label=(u'Password'), widget=forms.PasswordInput(render_value=False))
		



	
