from .models import GeoProduct
from rest_framework import serializers


class GeoProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoProduct
        fields = ['id', 'title', 'price', 'os_platform', 'description']
