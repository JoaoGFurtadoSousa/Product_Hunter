from django.shortcuts import get_object_or_404
from celery import shared_task
from .models import User
from django.core.mail import send_mail


verificy_code = 159753

@shared_task
def send_email_for_reset_password(email: str):
    user = get_object_or_404(User, email)
    send_mail()