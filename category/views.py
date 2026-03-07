from rest_framework.views import APIView
from .models import Category
from applications.models import APP
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from .serializers import CategorySerializer
from applications.serializers import APPSerializer


class CategoryView(APIView):
    permission_classes = [IsAuthenticated, DjangoModelPermissions]
    queryset = Category.objects.all()
    
    def get(self, request, pk=None):
        if pk:
            category = Category.objects.get(id = pk)
            return Response(CategorySerializer(category).data,  status= HTTP_200_OK)
        categorys = Category.objects.all()
        data_category = CategorySerializer(categorys, many = True)
        return Response(data_category.data)
    
    def post(self, request):
        data_request = CategorySerializer(data = request.data)
        if data_request.is_valid():
            category = Category.objects.create(name= data_request.validated_data['name'])
            category.save()
            return Response({"sucess": "Category created"}, status = HTTP_201_CREATED)
        return Response({"error": "Data invalid format"}, status = HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        data_request = CategorySerializer(data= request.data)
        if data_request.is_valid():
            category = get_object_or_404(Category, id = pk)
            category.name = data_request.validated_data['name']
            category.save()
            return Response({"sucess":"Category altered"}, status= HTTP_200_OK)
        
    def delete(self, request, pk):
            category = Category.objects.get(id = pk)
            category = get_object_or_404(Category, id = pk)
            category.delete()
            return Response({"sucess":"Category excluded"}, status= HTTP_200_OK)
    

class ReturnAPPsOfCategory(APIView):
     permission_classes = [IsAuthenticated, DjangoModelPermissions]
     queryset = APP.objects.all()

     def get(self, request, pk):
          apps = APP.objects.filter(category = pk)
          return Response(APPSerializer(apps, many = True).data, status= HTTP_200_OK)
          
          