from rest_framework.views import APIView
from applications.models import APP
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from .models import Vote

class LikeView(APIView):
   permission_classes = [IsAuthenticated, DjangoModelPermissions, ]
   queryset = Vote.objects.all()

   def post(self, request, pk: int):
        app = get_object_or_404(APP, id= pk)
        app.likes += 1
        app.save()
        return Response({'sucess': 'Like added'}, status=status.HTTP_200_OK)