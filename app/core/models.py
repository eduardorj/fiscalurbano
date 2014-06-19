from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    phone = models.IntegerField(max_length=13, unique=True, validators=[RegexValidator(regex='^\d{13}$', message='Length has to be 13', code='Invalid number')])