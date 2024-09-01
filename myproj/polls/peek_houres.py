from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost:3306/test data')
sale_receipts_df = pd.read_sql('SELECT * FROM salereciepts', con=engine)

# Convert the 'transaction_date' column to datetime format
sale_receipts_df['transaction_date'] = pd.to_datetime(sale_receipts_df['transaction_date'])


def peek_houres(sales_outlet_id):
    houres_list = ['transaction_date', 'transaction_time', 'sales_outlet_id']
    peek_houres = sale_receipts_df[houres_list]
    peek_houres = peek_houres[(peek_houres["sales_outlet_id"] == sales_outlet_id)]
    print(peek_houres.dtypes)
    peek_houres['hour'] = peek_houres['transaction_time'].apply(lambda x: x.seconds // 3600)

    peek_houres = peek_houres.groupby(['transaction_date', 'hour'])['hour'].count().reset_index(name='count')

    max_hour_per_day = peek_houres.loc[peek_houres.groupby('transaction_date')['count'].idxmax()].reset_index(drop=True)

    max_hour_per_day = max_hour_per_day.groupby('hour')['hour'].count().reset_index(name='count')
    #max_hour_per_day= max_hour_per_day.groupby(['hour','count'])['count'].max()



    print(max_hour_per_day)


if __name__ == '__main__':
    peek_houres(3)