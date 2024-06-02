from django.contrib import admin
from django.urls import path
from app.views import index, product_detail, product_grid, product_details

urlpatterns = [
    path('', index, name='index'),
    path('product-detail/<int:product_id>/', product_detail, name='product-detail'),
    path('product-grid/', product_grid, name='product-grid'),
    path('product-details/', product_details, name='product-details'),
]
