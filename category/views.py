from rest_framework.views import APIView
from .models import Category
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import CategorySerializer
# Create your views here.

class CategoryView(APIView):
    permission_classes = [IsAuthenticated, ]

    def get(self, request):
        categorys = Category.objects.all()
        print(categorys)
        return Response(CategorySerializer(categorys, many= True).data)
