from django.urls import path, include
from .views import CategoryView

urlpatterns = [
   path('category/', CategoryView.as_view(), name = 'category'),
   path('category/<int:pk>', CategoryView.as_view(), name = 'category')
]
