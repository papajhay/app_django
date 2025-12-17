from rest_framework import serializers
from .models import Product
from .serializers_mixins import CleanHTMLMixin

class ProductSerializer(serializers.ModelSerializer, CleanHTMLMixin):
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'image', 'created_at', 'updated_at']
       
