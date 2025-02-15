from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id, start_date, end_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, start_date=start_date, end_date=end_date,
                                   filtering_list=sales_list)
    return filtered_df


def get_total_items(sales_outlet_id, start_date, end_date):
    sales_df = filter_df(sales_outlet_id, start_date, end_date)
    grouped_sales_df = sales_df.groupby(['transaction_date'])['quantity'].sum().reset_index(name='item number')
    print(grouped_sales_df)
    return grouped_sales_df

get_total_items(3,'2019-04-01','2019-04-08')