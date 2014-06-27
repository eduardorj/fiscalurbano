from django.db import models
from app.fiscalizacao.models import UserProfile
from django.contrib.auth.models import User

def user_post_delete(sender, instance, **kwargs):
    try:
        UserProfile.objects.get(user=instance).delete()
    except:
        pass

def user_post_save(sender, instance, **kwargs):
    try:
        profile, new = UserProfile.objects.get_or_create(user=instance)
    except:
        pass

models.signals.post_delete.connect(user_post_delete, sender=User)
models.signals.post_save.connect(user_post_save, sender=User)