from rest_framework.views import APIView
from .serializers import APPSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import APP
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
# Create your views here.



class APPView(APIView):
    permission_classes = [IsAuthenticated, ]
    def get_object(self, pk: int):
      app = get_object_or_404(APP, pk = pk)


    def post(self, request):
       data_user = APPSerializer(data = request.data)
       if data_user.is_valid():
           data_user.save()
           return Response({"sucess": "App created"}, status= status.HTTP_201_CREATED)
       return Response({"error": "The data is in an invalid format"}, status= status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            return_all_apps = APP.objects.all()
            apps = APPSerializer(return_all_apps, many =  True).data
            return Response(apps, status= status.HTTP_200_OK)
        except:
            return Response({'error': 'Internal error'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk:int):
        app = self.get_object(pk = pk)  
        app.name = request.data.get('name')
        app.description = request.data.get('description')
        app.logo_app = request.data.get('logo_app')
        app.hashtags.set(request.data.get('hashtags'))
        app.save()
        return Response({"sucess":"App altered"}, status= status.HTTP_200_OK)
    
    def delete(self, request, pk: int):
        self.permission_classes = ['IsAuthenticated', ]
        app = APP.objects.filter(id = pk)
        app.delete()
        return Response({'sucess': 'App deleted'}, status=status.HTTP_200_OK)


