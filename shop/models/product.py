from django.db import models
# Create your models here.
from .category import Category

class Product(models.Model):
    # create fields
    product_name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    ptype = models.CharField(max_length=30, default="", blank=True)
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=500, default='', null=True, blank=True)
    total_item = models.IntegerField(default=0)
    image = models.ImageField(upload_to="products/", default="")

    # get all products and return
    #@staticmethod
    #def get_all_products():
    #    return Product.objects.all()
    # and now go to views.py and collect data in this

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.objects.all()


    def __str__(self):
        return self.product_name