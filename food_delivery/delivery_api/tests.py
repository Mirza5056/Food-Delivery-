from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class CalculatePriceViewAPITest(APITestCase):
    def test_get_request(self):
        url = reverse('calculate_price')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_post_request(self):
        url = reverse('calculate_price')
        data = {
            "zone": "central",
            "organization_id": "1",
            "total_distance": 12,
            "item_type": "perishable"
        }
        response = self.client.post(url, data, format='json')
        print(response.content)
        print(url)
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
