from app.fiscalizacao.models import Relato, Tag
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

class RelatoAdmin(admin.ModelAdmin):
	list_display = ('user', 'anonymous', 'incidentTitle', 'description', 'latitude', 'longitude', 'timestamp', 'get_tags')
	date_hierarchy = 'timestamp'
	list_filter = ('timestamp','incidentTitle',)

	def get_tags(self, obj):
		return "\n".join([p.name for p in obj.tags.all()])

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'size',)
	list_filter = ('name','size',)

admin.site.register(Relato, RelatoAdmin)
admin.site.register(Tag, TagAdmin)



#formfield_overrides = {
#    models.ManyToManyField: {'widget': CheckboxSelectMultiple},
#}