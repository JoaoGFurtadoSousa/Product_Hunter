from django.urls import path
from . import views


urlpatterns = [
    path('likes/<int:pk>', views.LikeView.as_view(), name = "add_like")
]