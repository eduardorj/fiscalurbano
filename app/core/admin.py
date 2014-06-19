from app.core.models import UserProfile
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User

#admin.site.unregister(User)

#class UserProfileInline(admin.StackedInline):
#    model = UserProfile

#class UserProfileAdmin(User):
#    inlines = [ UserProfileInline, ]

#admin.site.register(User, UserProfileAdmin)