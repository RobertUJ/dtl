from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('tracking.apps.main.views',
	url(r'^$','main_view',name='main_view'),
	# url(r'^contact/$','contact_view',name='contact_view'),
	# url(r'^pendientes/$','pendientes',name='pendientes_view'),
)

