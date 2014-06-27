#-*- coding: utf-8 -*-
from app.fiscalizacao.models import Relato, UserProfile
from rest_framework import serializers
from django.contrib.auth.models import User

class RelatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relato
        fields = ('id','anonymous', 'user', 'incidentTitle', 'description', 'latitude', 'longitude', 'timestamp', )

class UserSerializer(serializers.HyperlinkedModelSerializer):

    nick = serializers.SerializerMethodField('get_nick')
    mood = serializers.SerializerMethodField('get_mood')

    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'nick', 'mood',)

    def get_nick(self, obj):
        return obj.profile.nick

    def get_mood(self, obj):
        return obj.profile.mood