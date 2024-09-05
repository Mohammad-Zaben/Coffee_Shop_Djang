from myproj.polls.controllers.database import sale_receipts_df, pd


def receipt_daily_base(sales_outlet_id, day_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    sales_df = sale_receipts_df[sales_list]

    sales_df = sales_df[(sales_df["transaction_date"] == day_date) & (sales_df["sales_outlet_id"] == sales_outlet_id)]
    sales_df = sales_df.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))
    # Print the total sales sum
    return sales_df["total_sales"].sum()


def daily_logic(date_range, days_num, sales_outlet_id):
    daily_data = []

    for i in range(days_num):
        total_sales = receipt_daily_base(sales_outlet_id, date_range[i].to_pydatetime())
        daily_data.append({'Date': date_range[i].to_pydatetime(), 'total_sales': total_sales})

    daily_df = pd.DataFrame(daily_data)
    return daily_df


def weekly_logic(start_date, end_date, sales_outlet_id):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    weekly_df = sale_receipts_df[sales_list]
    weekly_df = weekly_df[
        (weekly_df["transaction_date"] >= start_date) & (weekly_df["transaction_date"] <= end_date) & (
                weekly_df["sales_outlet_id"] == sales_outlet_id)]
    weekly_df = weekly_df.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))

    weekly_df = weekly_df.assign(work_week=lambda x: x["transaction_date"].apply(lambda dt: dt.isocalendar()[1]))

    weekly_df = weekly_df.groupby('work_week')['total_sales'].sum().reset_index()
    return weekly_df


def logic_type(start_date, end_date, sales_outlet_id):
    date_range = pd.date_range(start=start_date, end=end_date)
    #print(date_range)
    days_num = len(date_range)
    result_df = None
    if days_num <= 7:
        result_df = daily_logic(date_range, days_num, sales_outlet_id)
    elif days_num <= 30:
        result_df = weekly_logic(start_date, end_date, sales_outlet_id)
    else:
        pass
    print(result_df)
    return result_df


if __name__ == '__main__':
    # Todo test for performance and logic
    start_date = '2019-04-01'
    end_date = '2019-04-18'
    sales_outlet_id = 3
    retail_data = logic_type(start_date, end_date, sales_outlet_id)

