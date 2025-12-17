from django.urls import path
from app.products import views  # ← importer depuis products

urlpatterns = [
    path('', views.home, name='home'),  # la page d'accueil
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
]
