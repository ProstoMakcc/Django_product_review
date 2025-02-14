from django.contrib import admin
from django.urls import path
from .views import product_list, product

urlpatterns = [
    path('', product_list, name="product_list"),
    path('products/<int:pk>/', product, name="product")
]