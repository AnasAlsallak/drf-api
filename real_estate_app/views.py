from django.shortcuts import render
from rest_framework import generics
from .models import RealEstate, RealEstateAgents
from .serializers import realEstateSerializer, realEstateDetailSerializer, realEstateAgentsSerializer, realEstateAgentsDetailSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsOwnerOrReadOnly

# Create your views here.

class RealEstateListView(generics.ListCreateAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = realEstateSerializer
    permission_classes = [AllowAny]

class RealEstateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RealEstate.objects.all()
    serializer_class = realEstateDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]

class RealEstateAgentsListView(generics.ListCreateAPIView):
    queryset = RealEstateAgents.objects.all()
    serializer_class = realEstateAgentsSerializer
    permission_classes =[IsAuthenticated]

class RealEstateAgentsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RealEstateAgents.objects.all()
    serializer_class =  realEstateAgentsDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]