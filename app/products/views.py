from rest_framework import viewsets
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from app.products.models import Product 

def home(request):
    products = Product.objects.all().order_by('-id')  # ou un autre tri si tu veux
    paginator = Paginator(products, 8)  # 8 produits par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/home.html', {'page_obj': page_obj})

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'pages/products/product_detail.html', {'product': product})