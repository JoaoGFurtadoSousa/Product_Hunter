from django.urls import path, include
from .views import CategoryView, ReturnAPPsOfCategory

urlpatterns = [
   path('category/', CategoryView.as_view(), name = 'category'),
   path('category/<int:pk>', CategoryView.as_view(), name = 'category'),
   path('category/apps/<int:pk>', ReturnAPPsOfCategory.as_view(), name = 'categorys-apps')
]
