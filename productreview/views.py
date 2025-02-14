from django.shortcuts import render
from .models import Product, Review

def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products
    }

    return render(request, "productreview/products_list.html", context)

def product(request, pk):
    product = Product.objects.get(pk=pk)
    reviews = Review.objects.filter(product=product)
    context = {
        "product": product,
        "reviews": reviews
    }

    return render(request, "productreview/product.html", context)