# delivery_api/views.py

from rest_framework import generics
from .models import Organization, Item, Pricing
from .serializers import OrganizationSerializer, ItemSerializer, PricingSerializer
from .services import PriceCalculator
from rest_framework.response import Response
from rest_framework.views import APIView

class OrganizationListCreateView(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PricingListCreateView(generics.ListCreateAPIView):
    queryset = Pricing.objects.all()
    serializer_class = PricingSerializer

class CalculatePriceView(APIView):
    def post(self, request, *args, **kwargs):
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = request.data.get('total_distance')
        item_type = request.data.get('item_type')

        response_data = PriceCalculator.calculate_price(zone, organization_id, total_distance, item_type)
        print(response_data)
        return Response(response_data)
