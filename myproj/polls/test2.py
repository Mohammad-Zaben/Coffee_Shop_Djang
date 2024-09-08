# myapp/views.py
from models import SalesReceipts
from pandas import DataFrame

def get_sorted_cars():
    # Query all Car objects
    sales = SalesReceipts.objects.all().values()

    # Convert the queryset to a pandas DataFrame
    df = DataFrame(sales)

    # Sort the DataFrame by 'price'
   # df_sorted_cars = df_cars.sort_values(by='')

    # Convert the sorted DataFrame back to a list of dictionaries
    sales = df.to_dict(orient='records')

    # Return the sorted cars as JSON
    print(sales)


get_sorted_cars()