from celery import shared_task
from .models import APP
from .integration_ia import verify_that_the_app_description_is_not_malicious, details_the_app_description


# @shared_task
# def talk_gemini_for_write_description(id: int):
#     app = APP.objects.get(id = id)
#     response = details_the_app_description(app.description)
#     if response:
#         app.description = response 
#         app.save()
#     app.delete()
    
@shared_task
def verify_description_is_not_malicious(id: int):
    app = APP.objects.get(id = id)
    response = verify_that_the_app_description_is_not_malicious(app.description)
    if response:
        app.description = response 
        app.save()
    app.delete()

    
