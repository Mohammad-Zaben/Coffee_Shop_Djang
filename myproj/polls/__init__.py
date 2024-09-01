from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

engine = create_engine('mysql+pymysql://root:@localhost:3306/test data')
sale_receipts_df = pd.read_sql('SELECT * FROM salereciepts', con=engine)

# Convert the 'transaction_date' column to datetime format
sale_receipts_df['transaction_date'] = pd.to_datetime(sale_receipts_df['transaction_date'])


# def receipts_daily_base(sales_outlet_id, day_date):
#     receipts_list = ['transaction_date', 'sales_outlet_id', 'transaction_id']
#     new_df = sale_receipts_df[receipts_list]
#     # Filter the DataFrame based on the date and sales_outlet_id
#     new_df1 = new_df[(new_df["transaction_date"] == day_date) & (new_df["sales_outlet_id"] == sales_outlet_id)]
#     # Calculate total sales and avoid SettingWithCopyWarning
#     new_df1 = new_df1.drop_duplicates(subset='transaction_id')
#     # Print number of receipts
#     return new_df1.shape[0]


def sales_daily_base(sales_outlet_id, day_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    sales_df = sale_receipts_df[sales_list]

    sales_df = sales_df[(sales_df["transaction_date"] == day_date) & (sales_df["sales_outlet_id"] == sales_outlet_id)]
    sales_df = sales_df.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))
    # Print the total sales sum
    return sales_df["total_sales"].sum()


def daily_logic(date_range, days_num, sales_outlet_id):
    total_sales = 0
    daily_df = pd.DataFrame(columns=['Date', 'total_sales'])
    for i in range(days_num):
        total_sales = sales_daily_base(sales_outlet_id, date_range[i].to_pydatetime())
        new_row = pd.DataFrame({'Date': [date_range[i].to_pydatetime()], 'total_sales': [total_sales]})
        daily_df = pd.concat([daily_df, new_row], ignore_index=True)
        # total_sales = total_sales + sales_daily_base(sales_outlet_id, date_range[i].to_pydatetime())

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
    days_num = len(date_range)
    result_df = None
    if days_num <= 7:
        result_df = daily_logic(date_range, days_num, sales_outlet_id)
    elif days_num <= 30:
        result_df = weekly_logic(start_date, end_date, sales_outlet_id)
    elif days_num <= 365:
        pass
    else:
        pass
    return result_df


if __name__ == '__main__':
    # Todo test for performance and logic
    start_date = '2019-04-01'
    end_date = '2019-04-12'
    sales_outlet_id = 3


    # df = logic_type(start_date, end_date, sales_outlet_id)
    # print(df)
    # Create histogram
