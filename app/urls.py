from django.conf.urls import patterns, url, include
from rest_framework import routers
from django.contrib import admin
from fiscalizacao import views
from core.views import *


admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'relatos', views.RelatoViewSet)
#router.register(r'users', views.UserViewSet)


urlpatterns = patterns('',
	(r'^$', homepage),
	(r'^tags$', tags),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
	url(r'^admin/', include(admin.site.urls)),
	(r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
	url('^users/$', views.UserViewSet.as_view()),
)