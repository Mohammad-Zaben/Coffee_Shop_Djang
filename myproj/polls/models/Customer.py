from django.db import models


class Customer(models.Model):
    customer_id = models.IntegerField(primary_key=True)
    home_store = models.CharField(max_length=100)
    customer_first_name = models.CharField(max_length=50)
    customer_email = models.CharField(max_length=100)
    customer_since = models.DateField()
    loyalty_card_number = models.CharField(max_length=15)
    birthdate = models.DateField()
    gender = models.CharField(max_length=1)
    birth_year = models.IntegerField()
