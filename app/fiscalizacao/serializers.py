from app.fiscalizacao.models import Relato
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class RelatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relato
        fields = ('anonymous', 'user', 'text', 'lat', 'lon', 'data')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')