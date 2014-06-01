#-*- coding: utf-8 -*-
from django.db import models

class Relato(models.Model):
	anonymous = models.BooleanField(verbose_name="Usuário anônimo", default=False)
	user = models.CharField(max_length=50, verbose_name="Usuário")
	incidentTitle = models.CharField(max_length=200, verbose_name="Título")
	description = models.CharField(max_length=200, verbose_name="Descrição")
	latitude = models.CharField(max_length=20, verbose_name='Latitude')
	longitude = models.CharField(max_length=20, verbose_name='Longitude')
	timestamp = models.DateField(verbose_name='Data Criação')
	
	def __unicode__(self):
		return self.user
	
	class Meta:
		verbose_name = u'Relato'
		verbose_name_plural = u'Relatos'