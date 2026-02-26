
from rest_framework.views import APIView
from .serializers import APPSerializer
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class APPView(APIView):
    def post(self, request):
       data_user = APPSerializer(data = request.data)
       if data_user.is_valid():
           data_user.save()
           return Response({"sucess": "App created"}, status= status.HTTP_201_CREATED)
       return Response({"error": "The data is in an invalid format"}, status= status.HTTP_400_BAD_REQUEST)


