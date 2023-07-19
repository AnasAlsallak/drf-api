from django.urls import path
from .views import RealEstateListView, RealEstateDetailView, RealEstateAgentsListView, RealEstateAgentsDetailView

urlpatterns = [
    path('', RealEstateListView.as_view(), name='realestate_list'),
    path('/<int:pk>/', RealEstateDetailView.as_view(), name='realestate_detail'),
    path('/agents/', RealEstateAgentsListView.as_view(), name='realestateagents_list'),
    path('/agents/<int:pk>/', RealEstateAgentsDetailView.as_view(), name='realestateagents_detail'),
]
