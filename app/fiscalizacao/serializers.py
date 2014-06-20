#-*- coding: utf-8 -*-
from app.fiscalizacao.models import Relato
from rest_framework import serializers
from django.contrib.auth.models import User


class RelatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relato
        fields = ('id','anonymous', 'user', 'incidentTitle', 'description', 'latitude', 'longitude', 'timestamp', )

class UserSerializer(serializers.HyperlinkedModelSerializer):

    mobile = serializers.SerializerMethodField('get_mobile')

    class Meta:
        model = User
        fields = ('url', 'username', 'first_name', 'last_name', 'email', 'mobile',)

    def get_mobile(self, obj):
    	foo = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    	return obj.get_profile().url


    #favourite_locations = serializers.SerializerMethodField('get_favourite_locations')


#    def get_mobile(self, obj):
#        return obj.get_profile().mobile

#    def get_favourite_locations(self, obj):
#        return obj.get_profile().favourite_locations