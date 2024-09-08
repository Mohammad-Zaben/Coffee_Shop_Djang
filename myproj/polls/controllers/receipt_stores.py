from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id, start_date, end_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'transaction_id']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, start_date=start_date, end_date=end_date,
                                   filtering_list=sales_list)
    return filtered_df


def get_total_receipt(sales_outlet_id, start_date, end_date):
    sales_df = filter_df(sales_outlet_id, start_date, end_date)
    grouped_sales_df = sales_df.groupby(['transaction_date', 'transaction_id']).size().reset_index(name='receipt_count')
    grouped_sales_df = grouped_sales_df.groupby(['transaction_date'])['transaction_id'].count().reset_index(
        name='receipt_number')
    return grouped_sales_df
