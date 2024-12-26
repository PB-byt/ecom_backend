from django.contrib import admin

# Register your models here.
from .models import Product,Pictures
admin.site.register(Product)
admin.site.register(Pictures)