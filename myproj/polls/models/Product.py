from django.db import models


class Product(models.Model):
    product_id = models.IntegerField(primary_key=True)
    product_group = models.CharField(max_length=50)
    product_category = models.CharField(max_length=40)
    product_type = models.CharField(max_length=40)
    product = models.CharField(max_length=100)
    product_description = models.CharField(max_length=200)
    unit_of_measure = models.CharField(max_length=20)
    current_wholesale_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_retail_price = models.DecimalField(max_digits=10, decimal_places=2)
    tax_exempt_yn = models.CharField(max_length=1)
    promo_yn = models.CharField(max_length=1)
    new_product_yn = models.CharField(max_length=1)

