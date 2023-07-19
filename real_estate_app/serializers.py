from rest_framework import serializers
from .models import RealEstate, RealEstateAgents

class realEstateSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

class realEstateDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstate
        fields = '__all__'

class realEstateAgentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateAgents
        fields = '__all__'

class realEstateAgentsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = RealEstateAgents
        fields = '__all__'
        