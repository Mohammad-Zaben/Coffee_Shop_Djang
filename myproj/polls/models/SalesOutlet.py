from django.db import models


class Salesoutlet(models.Model):
    sales_outlet_id = models.IntegerField(primary_key=True)
    sales_outlet_type = models.CharField(max_length=20)
    store_square_feet = models.IntegerField()
    store_address = models.CharField(max_length=150)
    store_city = models.CharField(max_length=50)
    store_state_province = models.CharField(max_length=2)
    store_telephone = models.CharField(max_length=15)
    store_postal_code = models.CharField(max_length=10)
    store_latitude = models.DecimalField(max_digits=9, decimal_places=6)
    store_longitude = models.DecimalField(max_digits=9, decimal_places=6)
    manager = models.CharField(max_length=40)
    neighborhood = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'salesoutlet'



