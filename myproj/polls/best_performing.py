from database import sale_receipts_df

def best_week(week):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    weekly_dataframe = sale_receipts_df[sales_list]
    weekly_dataframe = weekly_dataframe.assign(work_week=lambda x: x["transaction_date"].apply(lambda dt: dt.isocalendar()[1]))
    weekly_dataframe = weekly_dataframe.drop(columns=['transaction_date'])
    weekly_dataframe = weekly_dataframe[(weekly_dataframe["work_week"] == week)]
    weekly_dataframe = weekly_dataframe.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))
    weekly_dataframe = weekly_dataframe.groupby(['work_week','sales_outlet_id'])['total_sales'].sum().reset_index()
    # Retrieve the row with the maximum 'total_sales'
    weekly_dataframe = weekly_dataframe.loc[weekly_dataframe['total_sales'].idxmax()]
    return weekly_dataframe


if __name__ == '__main__':
    week = 14
    weekly_dataframe = best_week(week)
    print(weekly_dataframe)