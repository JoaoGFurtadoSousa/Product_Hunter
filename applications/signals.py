from .models import APP
from django.db.models.signals import post_save
from django.dispatch import receiver
from .tasks import talk_gemini_for_write_description


@receiver(post_save, sender = APP)
def post_save_app(sender, instance, **kwargs):
   talk_gemini_for_write_description.delay(instance.id)