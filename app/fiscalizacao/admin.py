from app.fiscalizacao.models import Relato
from django.contrib import admin

class RelatoAdmin(admin.ModelAdmin):
	pass
	
admin.site.register(Relato, RelatoAdmin)