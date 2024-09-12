from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime
from ..controllers.sales_aggregator import get_total_sales


@api_view(['GET'])
def get_sales(request):
    sales_outlet_id = request.GET.get('id')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    sales_type = request.GET.get('sales_type')

    if sales_outlet_id is None or start_date is None or end_date is None:
        return Response({"error": "Missing required parameters."}, status=400)

    try:
        sales_outlet_id = int(sales_outlet_id)
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')
        sales_type = str(sales_type)
    except ValueError as e:
        return Response({"error": f"Invalid parameter: {str(e)}"}, status=400)

    try:
        retail_data = get_total_sales(start_date, end_date, sales_outlet_id, sales_type)
        print(f'retail_data: {retail_data}')  # Debug output
        result = retail_data.to_dict(orient="records")
        return Response(result)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


@api_view(['GET'])
def test(request):
    return Response("hello world")