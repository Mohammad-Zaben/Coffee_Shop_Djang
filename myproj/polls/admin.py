from django.contrib import admin
from .models.Product import Product
from .models.Customer import Customer
from .models.SalesOutlet import SalesOutlet
from .models.SalesReceipts import SalesReceipts

# Register your models here.
admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(SalesOutlet)
admin.site.register(SalesReceipts)

