#-*- coding: utf-8 -*-
from app.fiscalizacao.models import Relato
from rest_framework import serializers


class RelatoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Relato
        fields = ('id','anonymous', 'user', 'incidentTitle', 'description', 'latitude', 'longitude', 'timestamp', )
