from rest_framework.decorators import api_view
from rest_framework.response import Response

from .api_methods import sales_daily_base


# Create your views here.
@api_view(['GET', 'POST'])
def get_sales_daily_bases(request, sales_id, day_date):
    print( day_date + "*************************")
    result = sales_daily_base(sales_id, day_date)
    return Response(result)


