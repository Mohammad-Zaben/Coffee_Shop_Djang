from django.db import models
from .SalesOutlet import SalesOutlet
from .Customer import Customer
from .Product import Product


class SalesReceipts(models.Model):
    transaction_id = models.IntegerField()
    transaction_date = models.DateField()
    transaction_time = models.DateTimeField()
    sales_outlet = models.ForeignKey(SalesOutlet, on_delete=models.CASCADE)
    staff_id = models.IntegerField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    instore_yn = models.CharField(max_length=1)
    order = models.IntegerField()
    line_item_id = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    line_item_amount = models.DecimalField(max_digits=4, decimal_places=2)
    unit_price = models.DecimalField(max_digits=4, decimal_places=2)
    promo_item_yn = models.CharField(max_length=1, default='N')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['transaction_id', 'transaction_date', 'transaction_time'],
                name='unique_migration_host_combination'
            )
        ]
