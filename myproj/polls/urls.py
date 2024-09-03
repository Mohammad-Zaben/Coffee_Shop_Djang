from django.urls import path
from . import views

urlpatterns = [
    path('sale_daily/', views.get_sales_daily_bases),
    path('most_selling_item/', views.get_most_selling_item),
    path('peek_hour/', views.get_peek_hour),

]
