from celery import shared_task
from .models import APP
from .integration_ia import details_the_app_description


@shared_task
def talk_gemini_for_write_description(id: int):
    app = APP.objects.get(id = id)
    response = details_the_app_description(app.description)
    app.description = response 
    app.save()   