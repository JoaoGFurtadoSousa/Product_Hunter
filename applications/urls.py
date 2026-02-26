from django.urls import path
from . import views


urlpatterns = [
    path('applications/', views.APPView.as_view(), name = "app"),
]
