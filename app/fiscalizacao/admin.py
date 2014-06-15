from app.fiscalizacao.models import Relato
from django.contrib import admin

class RelatoAdmin(admin.ModelAdmin):
	list_display = ('anonymous', 'user', 'incidentTitle', 'description', 'latitude', 'longitude', 'timestamp',)
	date_hierarchy = 'timestamp'
	list_filter = ('timestamp','incidentTitle',)
	
	
admin.site.register(Relato, RelatoAdmin)