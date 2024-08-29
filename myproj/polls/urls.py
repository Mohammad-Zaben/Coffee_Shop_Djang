from django.urls import path

from . import views

urlpatterns = [
    path('sale_daily/<int:id>&<str:date>', views.get_sales_daily_bases)
]
