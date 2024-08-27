from django.db import models
from django.db.models import UniqueConstraint

from .SalesOutlet import Salesoutlet
from .Product import Product


class Salereciepts(models.Model):
    transaction_id = models.IntegerField(
        primary_key=True)  # The composite primary key (transaction_id, transaction_date, transaction_time, sales_outlet_id, order_num, line_item_id, product_id) found, that is not supported. The first column is selected.
    transaction_date = models.DateField()
    transaction_time = models.TimeField()
    sales_outlet = models.ForeignKey(Salesoutlet, models.DO_NOTHING)
    staff_id = models.IntegerField(blank=True, null=True)
    store_yn = models.CharField(max_length=1, blank=True, null=True)
    order_num = models.IntegerField()
    line_item_id = models.IntegerField()
    product = models.ForeignKey(Product, models.DO_NOTHING)
    quantity = models.IntegerField(blank=True, null=True)
    line_item_amount = models.IntegerField(blank=True, null=True)
    unit_price = models.IntegerField(blank=True, null=True)
    promo_item_yn = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salereciepts'
        unique_together = (('transaction_id', 'transaction_date', 'transaction_time', 'sales_outlet', 'order_num',
                            'line_item_id', 'product'),)
