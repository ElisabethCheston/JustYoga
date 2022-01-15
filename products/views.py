from django.shortcuts import render
from .models import Product

# Create your views here.

def products(request):
    # Show all products, including sorting and search queries

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)