from datetime import datetime

from rest_framework.decorators import api_view
from rest_framework.response import Response
from myproj.polls.controllers.sales import logic_type
from myproj.polls.controllers.most_selling_item import selling_item
from myproj.polls.controllers.peek_houres import peek_houres


# Create your views here.
@api_view(['GET'])
def get_sales_daily_bases(request):
    sales_outlet_id = request.GET.get('id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if sales_outlet_id is None or start_date is None or end_date is None:
        return Response({"error": "Missing required parameters."}, status=400)

    try:
        sales_outlet_id = int(sales_outlet_id)
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        return Response({"error": f"Invalid parameter: {str(e)}"}, status=400)

    try:
        retail_data = logic_type(start_date, end_date, sales_outlet_id)
        print(f'retail_data: {retail_data}')  # Debug output
        result = retail_data.to_dict(orient="records")
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_most_selling_item(request):
    try:
        selling_item()
        return Response(selling_item())
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def get_peek_hour(request):
    sales_outlet_id = request.GET.get('id')

    if sales_outlet_id is None:
        return Response({"error": "Missing required parameters."}, status=400)

    try:
        sales_outlet_id = int(sales_outlet_id)
        peek_houre = peek_houres(sales_outlet_id)
        return Response(peek_houre)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
