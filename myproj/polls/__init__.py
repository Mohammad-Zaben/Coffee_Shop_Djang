from datetime import datetime
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost:3306/test data')

df = pd.read_sql('SELECT * FROM salereciepts', con=engine)

df['transaction_date'] = pd.to_datetime(df['transaction_date'])


def sales_daily_base(sales_outlet_id, day_date):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    new_df = df[sales_list]

    # Filter the DataFrame based on the date and sales_outlet_id
    new_df1 = new_df[(new_df["transaction_date"] == day_date) & (new_df["sales_outlet_id"] == sales_outlet_id)].copy()

    # Calculate total sales and avoid SettingWithCopyWarning
    new_df1.loc[:, "total_sales"] = new_df1["quantity"] * new_df1["unit_price"]

    # Print the total sales sum
    print(new_df1["total_sales"].sum())



# Example usage
day_date = "2019-04-01"
sales_daily_base(3, day_date)
