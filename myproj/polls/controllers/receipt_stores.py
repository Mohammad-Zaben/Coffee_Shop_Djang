from database import sale_receipts_df
from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id, start_date, end_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'transaction_id']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, start_date=start_date, end_date=end_date,
                                   filtering_list=sales_list)
    return filtered_df


def get_total_sales(sales_outlet_id, start_date, end_date, logic_type):
    sales_df = filter_df(sales_outlet_id, start_date, end_date)
    sales_df = sales_df["transaction_id"].unique()
    print(len(sales_df))



get_total_sales(3,"2019-04-01","2019-04-08","wwwww")