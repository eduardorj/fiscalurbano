from django.conf.urls import patterns, url, include
from rest_framework import routers
from django.contrib import admin
from fiscalizacao import views
from core.views import *

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'relatos', views.RelatoViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browseable API.
urlpatterns = patterns('',
	(r'^$', homepage),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)


'''

from django.conf.urls import patterns, url, include
from rest_framework import routers, generics
from fiscalizacao import views
from django.conf import settings


#router = routers.DefaultRouter()
#router.register(r'^relatos', views.RelatoViewSet)

urlpatterns = patterns('',
	(r'^$', homepage),
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

#url(r'relatos', include('rest_framework.urls', namespace='rest_framework')),
#url(r'^relatos/', generics.ListCreateAPIView.as_view(model=Relato)),

'''