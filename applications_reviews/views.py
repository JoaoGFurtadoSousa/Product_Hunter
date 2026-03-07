from rest_framework import viewsets
from applications_reviews.models import APPReview
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from applications_reviews.serializers import ReadAPPReviewSerializer, CreateAPPReviewSerializer


class APPReviewView(viewsets.ModelViewSet):
    queryset = APPReview.objects.all()
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return CreateAPPReviewSerializer
        return ReadAPPReviewSerializer

    def list(self, request):
        apps = APPReview.objects.order_by('-stars')
        serializer = self.get_serializer_class()
        return Response(serializer(apps, many = True).data)





