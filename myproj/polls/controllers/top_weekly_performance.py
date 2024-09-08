from myproj.polls.controllers.Filtering import Filter


def filter_df(week):
    sales_list = ['transaction_date', 'sales_outlet_id', 'quantity', 'unit_price']
    filtered_df = Filter.filter_df(
        filtering_list=sales_list)
    filtered_df = Filter.get_work_week_df(filtered_df)

    # weekly_dataframe = filtered_df.drop(columns=['transaction_date'])
    weekly_dataframe = filtered_df[(filtered_df["work_week"] == week)]
    return weekly_dataframe


def get_filter_df(weekly_df):
    weekly_df = Filter.get_work_week_df(weekly_df)
    weekly_df = Filter.apply_total_sales(weekly_df)
    return weekly_df


def get_best_week(weekly_df):
    weekly_df = weekly_df.groupby(['work_week', 'sales_outlet_id'])['total_sales'].sum().reset_index()
    # Retrieve the row with the maximum 'total_sales'
    weekly_df = weekly_df.loc[weekly_df['total_sales'].idxmax()]
    return weekly_df


def get_top_week(week):
    weekly_df = filter_df(week)
    weekly_df = get_filter_df(weekly_df)
    weekly_df = get_best_week(weekly_df)
    print(weekly_df)
    return weekly_df

get_top_week(14)
