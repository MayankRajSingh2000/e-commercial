from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.orders import Orders
from .models.contact import Contact


class AdminProduct(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'category']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category)
admin.site.register(Orders)
admin.site.register(Contact)

