from django.db import models
from django import forms
from django.db.models.signals import post_save
# Models
from django.contrib.auth.models import User


class UserProfile(models.Model):
	user		= models.ForeignKey(User,unique=True)
	mobile 		= models.CharField(max_length=150,null=True,blank=True)
	street		= models.CharField(max_length=250,null=True,blank=True)
	city 		= models.CharField(max_length=150,null=True,blank=True)
	state 		= models.CharField(max_length=250,null=True,blank=True)
	zip_code 	= models.CharField(max_length=10,null=True,blank=True)
	dtl_code 	= models.CharField(max_length=25,null=True,blank=True)
	license		= models.BooleanField(default=False)

	def __unicode__(self):
		_user = self.user
		if _user.first_name == "":
			return _user.username
		else:
			return "%s %s"%(_user.first_name,_user.last_name)
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
post_save.connect(create_user_profile, sender=User)
