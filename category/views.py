from rest_framework.views import APIView
from .models import Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK, HTTP_404_NOT_FOUND
from .serializers import CategorySerializer
# Create your views here.

class CategoryView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
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
            category = Category.objects.get(id = pk)
            if not category:
                return Response({"error": "Category not found"}, status= HTTP_404_NOT_FOUND)
            category.name = data_request.validated_data['name']
            category.save()
            return Response({"sucess":"Category altered"}, status= HTTP_200_OK)
    

