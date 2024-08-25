from django.db import models
from .SalesOutlet import SalesOutlet
from .Customer import Customer
from .Product import Product


class SalesReceipts(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    transaction_date = models.DateField()
    transaction_time = models.DateTimeField()
    sales_outlet_id = models.ForeignKey(SalesOutlet, on_delete=models.CASCADE)
    staff_id = models.IntegerField
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    instore_yn = models.CharField(max_length=1)
    order = models.IntegerField
    line_item_id = models.IntegerField
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField
    line_item_amount = models.DecimalField
    unit_price = models.DecimalField
    promo_item_yn = models.CharField


