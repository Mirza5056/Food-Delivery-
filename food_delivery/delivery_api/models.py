# delivery_api/models.py

from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)

class Item(models.Model):
    PERISHABLE = 'perishable'
    NON_PERISHABLE = 'non_perishable'
    
    TYPE_CHOICES = [
        (PERISHABLE, 'Perishable'),
        (NON_PERISHABLE, 'Non-perishable'),
    ]
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=255)

class Pricing(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    zone = models.CharField(max_length=50)
    base_distance_in_km = models.PositiveIntegerField(default=5)
    perishable_km_price = models.PositiveIntegerField(default=150)  # in cents
    non_perishable_km_price = models.PositiveIntegerField(default=100)  # in cents
    fix_price = models.PositiveIntegerField(default=1000)  # in cents
    def calculate_total_price(self, total_distance):
        if self.item.type == 'perishable':
            per_km_price = self.perishable_km_price
        else:
            per_km_price = self.non_perishable_km_price

        total_price = self.fix_price + per_km_price * max(0, total_distance - self.base_distance_in_km)
        return total_price