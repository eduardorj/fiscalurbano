#-*- coding: utf-8 -*-
from app.fiscalizacao.models import Relato, UserProfile
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
        fields = ('id', 'url', 'username', 'email', 'mobile',)

    def get_mobile(self, obj):
        
        profile = None
        
        try:
            profile = obj.get_profile()
        except UserProfile.DoesNotExist:
            profile = UserProfile.objects.get_or_create(user=obj, mobile="0000000000001")
            #profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
        
        return profile.mobile