from django.urls import path
from .views import CountryListView,CountryDetailView,search,by_region

urlpatterns = [
    path('',CountryListView.as_view(),name='home-page'),
    path('details/<int:pk>/',CountryDetailView.as_view(),name='country-details'),
    path('search/',search,name = 'country-search'),
    path('region/',by_region,name='region-search'),
]