from app.fiscalizacao.models import Relato, Tag
from django.contrib import admin
from django.db import models
from django.forms import CheckboxSelectMultiple

from app.fiscalizacao.models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	max_num = 1
	fk_name = 'user'
	can_delete = False

class UserAdmin(AuthUserAdmin):
	inlines = [UserProfileInline]

class RelatoAdmin(admin.ModelAdmin):
	list_display = ('user', 'anonymous', 'incidentTitle', 'description', 'latitude', 'longitude', 'timestamp', 'get_tags')
	date_hierarchy = 'timestamp'
	list_filter = ('timestamp','incidentTitle',)

	def get_tags(self, obj):
		return ", ".join(['#' + p.name for p in obj.tags.all()])

class TagAdmin(admin.ModelAdmin):
	list_display = ('name', 'size',)
	list_filter = ('name','size',)

admin.site.register(Relato, RelatoAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)