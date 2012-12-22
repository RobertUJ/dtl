from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    #Import urls.py's apps 
    url(r'^',include('tracking.apps.main.urls')),
    url(r'^',include('tracking.apps.accounts.urls')),

)
