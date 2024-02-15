import requests

url = "http://calculate_price/"
data = {
    "zone": "central",
    "organization_id": "1",
    "total_distance": 12,
    "item_type": "perishable"
}

response = requests.post(url, json=data)

print("Response status code:", response.status_code)
print("Response content:", response.content)
