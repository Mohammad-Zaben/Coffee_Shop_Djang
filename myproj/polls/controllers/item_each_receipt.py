from item_per_receipt import get_total_items
from receipt_stores import get_total_receipt


def calculate_items_per_receipt(transaction_id, sale_id, start_date, end_date):
    sales_df = get_total_items(sale_id, start_date, end_date, 'daily')
    receipt_df = get_total_receipt(sale_id, start_date, end_date)
    sales_df=sales_df.assign(spending_amount=lambda x: (sales_df['item_count'] / receipt_df['receipt_number']))
    print(sales_df)
   # sales_df.drop(['item_count'], axis=1, inplace=True)

   # return sales_df
calculate_items_per_receipt(1, 3, '2019-04-01', '2019-04-08')
