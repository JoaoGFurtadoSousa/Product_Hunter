from rest_framework.views import APIView
from .models import APP
from .serializers import APPSerializer
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination

class APPView(APIView):
    #permission_classes = [IsAuthenticated, ]


    def post(self, request):
       data_user = APPSerializer(data = request.data)
       if data_user.is_valid():
           data_user.save()
           return Response({"sucess": "App created"}, status= status.HTTP_201_CREATED)
       return Response({"error": "The data is in an invalid format"}, status= status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        try:
            return_all_apps = APP.objects.order_by('-likes')
            paginator = PageNumberPagination()
            paginator.page_size = 10
            result_paginator = paginator.paginate_queryset(return_all_apps, request)
            apps = APPSerializer(result_paginator, many =  True).data
            return paginator.get_paginated_response(apps)
        except:
            return Response({'error': 'Internal error'}, status= status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk:int):
        app = get_object_or_404(APP, id = pk)
        app.name = request.data.get('name')
        app.description = request.data.get('description')
        app.logo_app = request.data.get('logo_app')
        app.hashtags.set(request.data.get('hashtags'))
        app.save()
        return Response({"sucess":"App altered"}, status= status.HTTP_200_OK)
    
    def delete(self, request, pk: int):
        app = APP.objects.filter(id = pk)
        app.delete()
        return Response({'sucess': 'App deleted'}, status=status.HTTP_200_OK)

class SearchAPPForName(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        app_search = request.query_params.get('search_app')
        if not app_search:
            return Response({"error": "Parameters cannot be empty"}, status= status.HTTP_400_BAD_REQUEST)
        search_app_in_db =APP.objects.filter(name__icontains = app_search)
        if not search_app_in_db:
            return Response({"error": "APP not found"}, status= status.HTTP_404_NOT_FOUND)
        return Response(APPSerializer(search_app_in_db, many = True).data, status= status.HTTP_200_OK)
        

        
