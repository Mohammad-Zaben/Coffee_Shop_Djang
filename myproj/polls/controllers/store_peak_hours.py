import pandas as pd

from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id):
    houres_list = ['transaction_date', 'transaction_time', 'sales_outlet_id']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, filtering_list=houres_list)
    return filtered_df


def add_hour_column(peek_hour_df):
    peek_hour_df['hour'] = peek_hour_df['transaction_time'].dt.components.hours
    peek_hour_df = peek_hour_df.groupby(['transaction_date', 'hour'])['hour'].count().reset_index(name='count')
    return peek_hour_df

def extract_data():
    data = {
        'hour': [2, 3, 4, 5, 6],
        'count': [3, 3, 1, 1, 1],
    }

    return pd.DataFrame(data)


def get_max_hour(peek_hour_df):
    peek_hour_df = peek_hour_df.loc[peek_hour_df.groupby('transaction_date')['count'].idxmax()].reset_index(drop=True)
    peek_hour_df = peek_hour_df.groupby('hour')['hour'].count().reset_index(name='count')
    print(peek_hour_df)
    max_count_index = peek_hour_df['count'].idxmax()
    max_hour = peek_hour_df.loc[max_count_index, 'hour']

    #return max_hour


def get_peak_hour(sales_outlet_id):
    peek_hour_df = filter_df(sales_outlet_id)
    peek_hour_df = add_hour_column(peek_hour_df)
    print(peek_hour_df)
    peek_hour_df = get_max_hour(peek_hour_df)
    print(peek_hour_df)


get_peak_hour(3)

get_max_hour(extract_data())