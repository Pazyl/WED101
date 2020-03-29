from django.contrib import admin

from api.models import Product
from api.models import Category

admin.site.register(Product)
admin.site.register(Category)
