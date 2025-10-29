"""
url : https://dummyjson.com/products/add
payload: {
    "title": "BMW Pencil"

  }

header = { 'Content-Type': 'application/json' }

Method:POST


Resp:

{
    "id": 101,
    "title": "BMW Pencil"
}
"""
import requests
import json
url = "https://dummyjson.com/products/add"
payload = {"title": "BMW Pencil"}
header = {'Content-Type': 'application/json'}
response = requests.post(url=url, data=payload, headers=header,)
response_json = response.json()

print(response_json)
print(response.status_code)

# =====================================================================================

dummy_resp = {
    "id": 11,
    "title": "perfume Oil",
    "description": "Mega Discount, Impression of A...",
    "price": 13,
    "discountPercentage": 8.4,
    "rating": 4.26,
    "stock": 65,
    "brand": "Impression of Acqua Di Gio",
    "category": "fragrances",
    "thumbnail": "https://cdn.dummyjson.com/product-images-thumbnail/11/4.jpg",
    "images": [
        "https://cdn.dummyjson.com/product-images/11/1.jpg",
        "https://cdn.dummyjson.com/product-images/11/2.jpg",
        "https://cdn.dummyjson.com/product-images/11/3.jpg",
        "https://cdn.dummyjson.com/product-images-thumbnail/11/3.jpg"
    ]
}

thumbnail_values = [value for value in dummy_resp.values() if isinstance(value, str) and "thumbnail" in value]
print(thumbnail_values)

for value in thumbnail_values:
    print(value)


for key,value in dummy_resp.items():
    for image in value:
        if "thumbnail" in str(value):
             print(value)

for image in dummy_resp["images"]:
    if "thumbnail" in str(image):
        print(image)

# ===============================================================================================================

data = [20, 2, 6, 13, 4, 18, 8, 5, 0, 4, 10, 11, 2, 18, 20]
K = 8

for i in range(len(data)):
    for j in range(i + 1, len(data)):
        if data[i] + data[j] == 8:
            print(i, ",", j)
