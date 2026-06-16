from .models import APP
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import verify_description_is_not_malicious


@receiver(post_save, sender = APP)
def post_save_app(sender, instance, created, **kwargs):
   if created:
      print(f"Enfileirando APP {instance.id}")
      response = verify_description_is_not_malicious.delay(instance.id)
      print(response)

         