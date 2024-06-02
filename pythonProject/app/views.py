from django.shortcuts import render

from app.models import Product, Customers


# Create your views here.


def index(request):
    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'app/index.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'app/product-details.html', context)

def add_customers(request):
    customers = Customers.objects.all()
    context = {
        'customer': customers
    }
    return render(request, 'app/product-details.html', context)
def product_grid(request):
    products = Product.objects.all()
    return render(request, 'app/product-grid.html')
def product_details(request):
    return render(request, 'app/product-details.html')