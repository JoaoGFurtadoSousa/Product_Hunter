from rest_framework import serializers
from .models import APP


class APPSerializer(serializers.ModelSerializer):
    class Meta:
        model = APP
        fields = ('name', 'description', 'likes', 'logo_app','hashtags',)