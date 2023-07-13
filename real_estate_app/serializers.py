from rest_framework import serializers
from .models import RealEstate

class realEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

class realEstateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'