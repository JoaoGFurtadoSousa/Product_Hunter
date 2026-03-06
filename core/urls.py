from django.contrib import admin
from django.urls import path, include
from users.views import Login_User, RegisterUser
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',Login_User.as_view(), name= 'login_user'),
    path('register/', RegisterUser.as_view(), name = 'register_user'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/', include('applications.urls')),
    path('api/v1/', include('votes.urls')),
    path('api/v1/', include('category.urls')),
]
