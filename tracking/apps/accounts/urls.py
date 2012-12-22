from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('tracking.apps.accounts.views',
	url(r'^register.accounts/$','register_user',name='register_view'),
	# url(r'^contact/$','contact_view',name='contact_view'),
	# url(r'^pendientes/$','pendientes',name='pendientes_view'),
)

