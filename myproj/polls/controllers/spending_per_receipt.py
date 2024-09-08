from sales_aggregator import get_total_sales
from receipt_stores import get_total_receipt


def get_spending(sale_id, start_date, end_date):
    sales_df = get_total_sales(sale_id, start_date, end_date, 'daily')
    receipt_df = get_total_receipt(sale_id, start_date, end_date)
    sales_df = sales_df.assign(spending_amount=lambda x: (sales_df['total_sales'] / receipt_df['receipt_number']))
    print(sales_df)
    return sales_df

get_spending(3, '2019-04-01', '2019-04-08')
