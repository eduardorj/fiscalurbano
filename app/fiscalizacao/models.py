#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
#from django.core.validators import RegexValidator


class Tag(models.Model):
	name = models.SlugField(max_length=20, verbose_name="Tag", db_index=True, unique=True, help_text="Nome da Tag exibida no portal")
	size = models.IntegerField(verbose_name="Tamanho da fonte", help_text="Tamanho da fonte que será exibido na Cloud", default=1)

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = u'Tag'
		verbose_name_plural = u'Tags'

class Relato(models.Model):
	anonymous = models.BooleanField(verbose_name="Usuário anônimo", default=False)
	user = models.CharField(max_length=50, verbose_name="Usuário")
	incidentTitle = models.CharField(max_length=200, verbose_name="Título")
	description = models.CharField(max_length=200, verbose_name="Descrição")
	latitude = models.CharField(max_length=20, verbose_name='Latitude')
	longitude = models.CharField(max_length=20, verbose_name='Longitude')
	timestamp = models.DateField(verbose_name='Data Criação')
	tags = models.ManyToManyField(Tag, verbose_name='Tags')

	#def get_tags(self):
	#	return ", ".join(['#' + p.name for p in self.tags.all()])

	def __unicode__(self):
		return self.user
	
	class Meta:
		verbose_name = u'Relato'
		verbose_name_plural = u'Relatos'

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, related_name="user_profile")
    url = models.URLField("Website", blank=True)
    company = models.CharField(max_length=50, blank=True)

    def __unicode__(self):
    	return self.user

	class Meta:
		verbose_name = u'Usuário'
		verbose_name_plural = u'Usuários'


    #User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])


"""
class UserProfile(models.Model):
	user = models.ForeignKey(User, unique=True)
	phone = models.IntegerField(max_length=13, unique=True, validators=[RegexValidator(regex='^\d{13}$', message='Length has to be 13', code='Invalid number')])

	def __unicode__(self):
		return self.phone

	class Meta:
		verbose_name = u'Usuário'
		verbose_name_plural = u'Usuários'
"""