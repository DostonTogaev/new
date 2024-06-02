from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import Product, ProductAttribute, Image, Attribute

# Register your models here.


admin.site.register(Product)
admin.site.register(Image)
admin.site.register(ProductAttribute)
admin.site.register(Attribute)

admin.site.unregister(User)
admin.site.unregister(Group)