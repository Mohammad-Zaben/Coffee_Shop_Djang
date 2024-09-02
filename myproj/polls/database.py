from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('mysql+pymysql://root:@localhost:3306/test_data')
sale_receipts_df = pd.read_sql('SELECT * FROM salereciepts', con=engine)
# Convert the 'transaction_date' column to datetime format
sale_receipts_df['transaction_date'] = pd.to_datetime(sale_receipts_df['transaction_date'])