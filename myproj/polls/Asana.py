from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost:3306/test_data')
df = pd.read_sql('SELECT * FROM salereciepts', con=engine)
df['transaction_date'] = pd.to_datetime(df['transaction_date'])


def sales_daily_base(sales_outlet_id, day_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    new_df = df[sales_list]

    new_df1 = new_df[(new_df["transaction_date"] == day_date) & (new_df["sales_outlet_id"] == sales_outlet_id)]
    new_df1 = new_df1.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))
    # Print the total sales sum
    return new_df1["total_sales"].sum()


def daily_logic(date_range, days_num, sales_outlet_id):
    total_sales = 0
    for i in range(days_num):
        total_sales = total_sales + sales_daily_base(sales_outlet_id, date_range[i].to_pydatetime())
    return total_sales


def weekly_logic(start_date, end_date, sales_outlet_id):
    date_range = pd.date_range(start=start_date, end=end_date, freq='W')


def logic_type(start_date, end_date, sales_outlet_id):
    date_range = pd.date_range(start=start_date, end=end_date)
    days_num = len(date_range)
    total_sales = 0
    if (days_num <= 7):
        total_sales = daily_logic(date_range, days_num, sales_outlet_id)
    elif (days_num < 30):
        pass
    elif (days_num <= 365):
        pass
    else:
        pass

    return total_sales


if __name__ == '__main__':
    start_date = '2019-04-01'
    end_date = '2019-04-05'
    sales_outlet_id = 3

    x = logic_type(start_date, end_date, sales_outlet_id)
    print(x)
