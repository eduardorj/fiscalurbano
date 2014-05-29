#-*- coding: utf-8 -*-
from django.db import models

class Relato(models.Model):
	anonymous = models.BooleanField(verbose_name="Usuário anônimo", default=False)
	user = models.CharField(max_length=50, verbose_name="Usuário")
	text = models.CharField(max_length=200, verbose_name="Texto")
	lat = models.CharField(max_length=20, verbose_name='Latitude')
	lon = models.CharField(max_length=20, verbose_name='Longitude')
	data = models.DateField('Data criacao', auto_now_add=True)
	
	def __unicode__(self):
		return self.user
	
	class Meta:
		verbose_name = u'Relato'
		verbose_name_plural = u'Relatos'