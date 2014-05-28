#from django.conf.urls.defaults import *
from django.conf.urls import patterns, url, include
from core.views import *
from django.conf import settings

from django.contrib import admin

admin.autodiscover()


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'fcontrol.views.home', name='home'),
    # url(r'^fcontrol/', include('fcontrol.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	(r'^$', homepage),
	(r'^kml$', generateKml),
	(r'^event/save-json/$', save_events_json),
)

#from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()

#urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'app.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)