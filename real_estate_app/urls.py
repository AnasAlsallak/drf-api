from django.urls import path
from .views import RealEstateListView, RealEstateDetailView

urlpatterns = [
    path('', RealEstateListView.as_view(), name='realestate_list'),
    path('/<int:pk>/', RealEstateDetailView.as_view(), name='realestate_detail'),
]
