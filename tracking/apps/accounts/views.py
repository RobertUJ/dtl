#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives 
from django.http import HttpResponseRedirect, HttpResponse
# Modulos
from django.contrib.auth.models import User
# Formularios
from tracking.apps.accounts.forms import frmUserReg,frmUserProf,LoginForm



def register_user(request):
	if request.method == "POST":
		frm_user = frmUserReg(request.POST)
		# frm_profile = frmUserProf(request.POST)
		if frm_user.is_valid():
			username_ = frm_user.cleaned_data['username']
			email_ = frm_user.cleaned_data['email']
			password_ = frm_user.cleaned_data['password']
			new_user = User.objects.create_user(username= username_, email= email_,password=password_)
			new_user.is_staff = False
			new_user.first_name = frm_user.cleaned_data['first_name']
			new_user.last_name 	= frm_user.cleaned_data['last_name']
			new_user.save()
			return HttpResponseRedirect('/')
	else:
		frm_user = frmUserReg()
		# frm_profile = frmUserProf()
	ctx = {'form':frm_user}
	return render_to_response('forms/accounts/register.html',ctx,context_instance=RequestContext(request))

