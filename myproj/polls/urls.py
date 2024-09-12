from django.urls import path
from .API_controllers import sales_API

urlpatterns = [
    path('total_sales/', sales_API.get_sales)
    # path('most_selling_item/', views.get_most_selling_item),
    # path('peek_hour/', views.get_peek_hour),

]
