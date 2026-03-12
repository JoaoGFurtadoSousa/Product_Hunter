from .models import APP
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender = APP)
def post_save_app(sender, instance, **kwargs):
    print(instance.description)