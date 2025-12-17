import requests

url = 'http://127.0.0.1:8000/api/products/product/'
data = {
    'name': 'Test Product',
    'price': '49.99',
    'description': 'Produit de test'
}
files = {'image': open('C:/dev/crud-django/media/products/box.jpeg', 'rb')}

response = requests.post(url, data=data, files=files)
print(response.status_code)
print(response.json())
