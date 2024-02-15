# delivery_api/services.py
from django.core.exceptions import ObjectDoesNotExist
from .models import Organization, Item, Pricing
class PriceCalculator:
    @staticmethod
    def calculate_price(zone, organization_id, total_distance, item_type):
        try:
            pricing = Pricing.objects.get(
                organization_id=organization_id,
                item__type=item_type,
                zone=zone,
                base_distance_in_km__lte=total_distance,
            )
            total_price = pricing.calculate_total_price(int(total_distance))
            return {'total_price': total_price / 100.0}
        except ObjectDoesNotExist:
            return None
