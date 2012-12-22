#encoding:utf-8
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.core.mail import EmailMultiAlternatives 
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User



def main_view(request):
	return render_to_response('home/home.html',context_instance=RequestContext(request))