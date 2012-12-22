from django import forms
from django.forms import ModelChoiceField
from django.core import validators
from django.core.exceptions import ValidationError
from django.forms import ModelForm 
from django.db import models
# models
from tracking.apps.accounts.models import UserProfile
from django.contrib.auth.models import User


# Functions

def validate_username_unique(value):
	''' Custom validator for user uniqueness. '''
	if User.objects.filter(username=value).exists():
		raise ValidationError(u'The username "%s" is already taken.' % value)

def validate_email_unique(value):
	''' Custom validator for user uniqueness. '''
	if User.objects.filter(email=value).exists():
		raise ValidationError(u'The email "%s" is already taken.' % value)


#  Classs Forms

class LoginForm(forms.Form):
		username 		= forms.CharField(widget=forms.TextInput())
		password 		= forms.CharField(widget=forms.PasswordInput(render_value=False))


class frmUserProf(forms.ModelForm):
	class Meta:
		model = UserProfile
		exclude =['user','']


class frmUserReg(forms.Form):
	#UserName Field
	username	=	forms.CharField(
		max_length=20,
		widget=forms.TextInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
		min_length=3,
		validators=[validate_username_unique]
	)
	#Email Field
	email 	= 	forms.EmailField(
		max_length=255,
		widget=forms.TextInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
		validators=[validate_email_unique]

	)
	# Password & Re-Password
	password 	= 	forms.CharField(
		max_length=20,
		widget=forms.PasswordInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
	)
	repassword 	= 	forms.CharField(
		max_length=20,
		widget=forms.PasswordInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
	)
	# First Name
	first_name = forms.CharField(
		max_length=150,
		widget=forms.TextInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
	)
	# Last Name
	last_name = forms.CharField(
		max_length=150,
		widget=forms.TextInput(
			attrs={'class':'','placeholder':''},
		),
		required=True,
	)

 	def clean(self):
 		''' Required custom validation for the form. '''
 		super(forms.Form,self).clean()
 		if 'password' in self.cleaned_data and 'repassword' in self.cleaned_data:
 			if self.cleaned_data['password'] != self.cleaned_data['repassword']:
 				self._errors['password'] = [u'Passwords must match.']
				self._errors['repassword'] = [u'Password must match']
		return self.cleaned_data




