from rest_framework import serializers
from applications.serializers import APPSerializer
from .models import APPReview





class ReadAPPReviewSerializer(serializers.ModelSerializer):
    app = APPSerializer()
    class Meta:
        model = APPReview
        fields = ('app', 'stars', )

class CreateAPPReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = APPReview
        fields = '__all__'