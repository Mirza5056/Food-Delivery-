# delivery_api/urls.py

from django.urls import path
from .views import OrganizationListCreateView, ItemListCreateView, PricingListCreateView, CalculatePriceView

urlpatterns = [
    path('organizations/', OrganizationListCreateView.as_view(), name='organization-list-create'),
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('pricing/', PricingListCreateView.as_view(), name='pricing-list-create'),
    path('calculate_price/', CalculatePriceView.as_view(), name='calculate_price'),
]
