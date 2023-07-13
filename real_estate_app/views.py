from django.shortcuts import render
from rest_framework import generics
from .models import RealEstate
from .serializers import realEstateSerializer, realEstateDetailSerializer

# Create your views here.

class RealEstateListView(generics.ListCreateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = realEstateSerializer

class RealEstateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = realEstateDetailSerializer
