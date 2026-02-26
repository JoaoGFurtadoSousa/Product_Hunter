from django.urls import path
from . import views


urlpatterns = [
    path('applications/', views.APPView.as_view(), name = "app"),
    path('applications/<int:pk>/', views.APPView.as_view(), name = "app_unique"),
]
