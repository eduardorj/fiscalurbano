from django.conf.urls import patterns, url, include
from rest_framework import routers
from fiscalizacao import views
from django.conf import settings
from core.views import *

from django.contrib import admin

admin.autodiscover()

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'relatos', views.RelatoViewSet)

urlpatterns = patterns('',
    (r'^$', homepage),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)