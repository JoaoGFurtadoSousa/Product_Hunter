from .models import APP
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

@receiver(pre_save, sender = APP)
def pre_save_app(sender, instance, **kwargs):
    print(instance)