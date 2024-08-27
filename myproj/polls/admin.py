from django.contrib import admin
from .models.Product import Product
from .models.Customer import Customer
from .models.SalesOutlet import Salesoutlet
from .models.SalesReceipts import Salereciepts

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Salesoutlet)
admin.site.register(Salereciepts)

