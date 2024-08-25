from django.db import models
from .SalesOutlet import SalesOutlet
from .Customer import Customer
from .Product import Product


class SalesReceipts(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    transaction_date = models.DateField()
    transaction_time = models.DateTimeField()
    sales_outlet = models.ForeignKey(SalesOutlet, on_delete=models.CASCADE)
    staff_id = models.IntegerField(default=0)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    instore_yn = models.CharField(max_length=1)
    order = models.IntegerField(default=0)
    line_item_id = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    line_item_amount = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    unit_price = models.DecimalField(max_digits=4, decimal_places=2,default=0.0)
    promo_item_yn = models.CharField(max_length=1,default='N')


