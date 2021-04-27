from django.contrib import admin

from e_api.models import Category, Book, Product

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Book)