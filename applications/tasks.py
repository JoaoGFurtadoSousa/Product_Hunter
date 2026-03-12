from celery import shared_task
from .models import APP


@shared_task
def details_the_app_description(id: int):
    app = APP.objects.get(id = id)
    print(app)