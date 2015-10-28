from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegistrationForm(forms.Form):
	username = forms.CharField(label='Username', max_length=30)
	email = forms.EmailField(label='Email')
	password1 = forms.CharField(
		label='Password',
		widget=forms.PasswordInput()
	)
	password2 = forms.CharField(
	label='Password (Again)',
	widget=forms.PasswordInput()
	)
	
def clean_password2(self):
	if 'password1' in self.cleaned_data:
		password1 = self.cleaned_data['password1']
		password2 = self.cleaned_data['password2']
		if password1 == password2:
			return password2
	raise forms.ValidationError('Passwords do not match.')
	
def clean_username(self):
	username = self.cleaned_data['username']
	if not re.search(r'^\w+$', username):
		raise forms.ValidationError('Username can only contain alphanumeric characters and the underscore.')
	try:
		User.objects.get(username=username)
	except ObjectDoesNotExist:
		return username
	raise forms.ValidationError('Username is already taken.')
	
class QuizSaveForm(forms.Form):
	title = forms.CharField(
		label='Title',
		widget=forms.TextInput(attrs={'size': 60})
	)
	question = forms.CharField(
		label='Question',
		required=False,
		widget=forms.TextInput(attrs={'size': 60})
	)
	
	choice1 = forms.CharField(
		label='Choice 1',
		required=False,
		widget=forms.TextInput(attrs={'size': 60})
	)
	
	choice2 = forms.CharField(
		label='Choice 2',
		required=False,
		widget=forms.TextInput(attrs={'size': 60})
	)
	
	choice3 = forms.CharField(
		label='Choice 3',
		required=False,
		widget=forms.TextInput(attrs={'size': 60})
	)
	
	choice4 = forms.CharField(
		label='Choice 4',
		required=False,
		widget=forms.TextInput(attrs={'size': 60})
	)
	
	answer = forms.IntegerField(
		label='Answer',
		required=False,
		widget=forms.TextInput(attrs={'size': 4})
	)
