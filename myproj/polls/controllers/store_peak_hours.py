from myproj.polls.controllers.Filtering import Filter


def filter_df(sales_outlet_id):
    hours_list = ['transaction_date', 'transaction_time', 'sales_outlet_id']
    filtered_df = Filter.filter_df(sales_outlet_id=sales_outlet_id, filtering_list=hours_list)
    return filtered_df


def add_hour_column(peek_hour_df):
    peek_hour_df['hour'] = peek_hour_df['transaction_time'].dt.components.hours
    peek_hour_df = peek_hour_df.groupby(['transaction_date', 'hour'])['hour'].count().reset_index(name='count')
    return peek_hour_df


def get_max_hour(peek_hour_df):
    peek_hour_df = peek_hour_df.loc[peek_hour_df.groupby('transaction_date')['count'].idxmax()].reset_index(drop=True)
    peek_hour_df = peek_hour_df.groupby('hour')['hour'].count().reset_index(name='count')
    max_count = peek_hour_df['count'].max()
    peak_hours = peek_hour_df[peek_hour_df['count'] == max_count]['hour'].tolist()
    return peak_hours


def get_peak_hour(sales_outlet_id):
    peek_hour_df = filter_df(sales_outlet_id)
    peek_hour_df = add_hour_column(peek_hour_df)
    peek_hour = get_max_hour(peek_hour_df)
    print(peek_hour)

get_peak_hour(3)