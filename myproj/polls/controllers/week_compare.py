from myproj.polls.controllers.database import sale_receipts_df
from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, filtering_list=sales_list)
    return filtered_df


def calculate_weeks_sale(sales_df):
    sales_df = Filter.get_work_week_df(sales_df)
    sales_df = Filter.apply_total_sales(sales_df)
    sales_df.drop(['transaction_date'], axis=1, inplace=True)
    sales_df = sales_df.groupby(['work_week'])['total_sales'].sum().reset_index()

    return sales_df


def weeks_compare(sales_outlet_id, week_number):
    sales_df = filter_df(sales_outlet_id)
    sales_df = calculate_weeks_sale(sales_df)
    if week_number in sales_df['work_week'].values and week_number-1 in sales_df['work_week'].values:
        week_row = sales_df[sales_df['work_week'] == week_number]
        perv_week_row = sales_df[sales_df['work_week'] == week_number-1]
        print(week_row)
        print(perv_week_row)



weeks_compare(3, 15)
