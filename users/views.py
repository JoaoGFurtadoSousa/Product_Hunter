from django.contrib.auth import authenticate
from .models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework import status
from django.db.models import Q

class Login_User(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request= request, username= username, password= password)
        print(user)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({"acess_token": str(refresh.access_token),
                             "refresh_token":str(refresh)})
        return Response({"error": "User not found"}, status= status.HTTP_401_UNAUTHORIZED)
    
class RegisterUser(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(Q(email = email) | Q(username = username)).exists():
            print('entrou aqui')
            return Response({"error": "User already exists"}, status=status.HTTP_409_CONFLICT)
        User.objects.create_user(username= username, email= email, password= password)
        return Response({"sucess": "Create User"}, status=status.HTTP_201_CREATED)