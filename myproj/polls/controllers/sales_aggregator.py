from myproj.polls.controllers.database import sale_receipts_df
from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id, start_date, end_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, start_date=start_date, end_date=end_date,
                                   filtering_list=sales_list)
    return filtered_df


def apply_total_sales(filtered_df):
    filtered_df = filtered_df.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))
    return filtered_df


def get_work_week_df(sales_df):
    sales_df = sales_df.assign(work_week=lambda x: x["transaction_date"].apply(lambda dt: dt.isocalendar()[1]))
    return sales_df


def get_total_sales(sales_outlet_id, start_date, end_date, logic_type):
    sales_df = filter_df(sales_outlet_id, start_date, end_date)
    sales_df = apply_total_sales(sales_df)
    if logic_type == 'daily':
        sales_df = sales_df.groupby(['transaction_date'])['total_sales'].sum().reset_index()
        return sales_df
    elif logic_type == 'weekly':
        sales_df = get_work_week_df(sales_df)
        sales_df.drop(['transaction_date'], axis=1, inplace=True)
        sales_df = sales_df.groupby(['work_week'])['total_sales'].sum().reset_index()
        return sales_df
    else:
        print('Invalid logic type')


print(get_total_sales(3, '2019-04-01', '2019-04-05', 'daily'))