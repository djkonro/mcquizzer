from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re

class RegistrationForm(forms.Form):
    username = forms.CharField(
                               label='Username', 
                               max_length=30, 
                               widget=forms.TextInput(attrs={'class':'form-control', 'autofocus':'autofocus', 'required':'required', 'title':'Username'})
                               )
    email = forms.EmailField(
                             label='Email',
                             widget=forms.EmailInput(attrs={'class':'form-control', 'required':'required', 'title':'Email'})
                             )
    password1 = forms.CharField(
                                label='Password',
                                widget=forms.PasswordInput(attrs={'class':'form-control', 'required':'required', 'title':'Password'})
                                )
    password2 = forms.CharField(
                                label='Password (Again)',
                                widget=forms.PasswordInput(attrs={'class':'form-control', 'required':'required', 'title':'Password Second'})
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
                            widget=forms.TextInput(attrs={'size': 60, 'class':'form-control', 'autofocus':'autofocus', 'required':'required', 'title':'Title of Quiz'})
                            )
	
    time = forms.IntegerField(
                              label='Time in minutes',
                              required=False,
                              widget=forms.NumberInput(attrs={'size': 10, 'class':'form-control', 'required':'required', 'title':'Time'})
                              )
	
class QuestionSaveForm(forms.Form):
    question = forms.CharField(
                               label='Question',
                               required=False,
                               widget=forms.TextInput(attrs={'size': 60, 'class':'form-control', 'autofocus':'autofocus', 'required':'required', 'title':'Question'})
                               )
	
    choice1 = forms.CharField(
                              label='Choice 1',
                              required=False,
                              widget=forms.TextInput(attrs={'size': 45, 'class':'form-control', 'required':'required', 'title':'First choice'})
                              )
	
    choice2 = forms.CharField(
                              label='Choice 2',
                              required=False,
                              widget=forms.TextInput(attrs={'size': 45, 'class':'form-control', 'required':'required', 'title':'Second choice'})
                              )
	
    choice3 = forms.CharField(
                              label='Choice 3',
                              required=False,
                              widget=forms.TextInput(attrs={'size': 45, 'class':'form-control', 'required':'required', 'title':'Second choice'})
                              )
	
    choice4 = forms.CharField(
                              label='Choice 4',
                              required=False,
                              widget=forms.TextInput(attrs={'size': 45, 'class':'form-control', 'required':'required'})
                              )
	
    answer = forms.IntegerField(
                                label='Answer',
                                required=False,
                                widget=forms.NumberInput(attrs={'class':'form-control', 'size':10, 'required':'required'})
                                )
