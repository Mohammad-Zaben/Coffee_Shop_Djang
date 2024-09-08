from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id, start_date, end_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, start_date=start_date, end_date=end_date,
                                   filtering_list=sales_list)
    return filtered_df


def get_total_sales(sales_outlet_id, start_date, end_date, logic_type):
    sales_df = filter_df(sales_outlet_id, start_date, end_date)
    sales_df = Filter.apply_total_sales(sales_df)
    if logic_type == 'daily':
        sales_df = sales_df.groupby(['transaction_date'])['total_sales'].sum().reset_index()
        return sales_df
    elif logic_type == 'weekly':
        sales_df = Filter.get_work_week_df(sales_df)
        sales_df.drop(['transaction_date'], axis=1, inplace=True)
        sales_df = sales_df.groupby(['work_week'])['total_sales'].sum().reset_index()
        return sales_df
    else:
        print('Invalid logic type')


if __name__ == '__main__':
    # Todo test for performance and logic
    start_date = '2019-04-01'
    end_date = '2019-04-28'
    sales_outlet_id = 3
    retail_data = get_total_sales(sales_outlet_id, start_date, end_date, "weekly")
    print(retail_data)
