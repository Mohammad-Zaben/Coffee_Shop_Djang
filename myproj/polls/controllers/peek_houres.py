from matplotlib import pyplot as plt

import seaborn as sns

from myproj.polls.controllers.database import sale_receipts_df


def sales_scatter_plot(max_hour_per_day):
    plt.figure(figsize=(10, 6))
    plt.scatter(max_hour_per_day['count'], max_hour_per_day['hour'], color='blue', marker='o')
    plt.title('Sales Scatter Plot')
    plt.xlabel('count')
    plt.ylabel('hour')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.yticks(max_hour_per_day["hour"])
    plt.grid(True)
    plt.show()


# def peek_houres(sales_outlet_id):
#     houres_list = ['transaction_date', 'transaction_time', 'sales_outlet_id']
#     peek_houres = sale_receipts_df[houres_list]
#     peek_houres = peek_houres[(peek_houres["sales_outlet_id"] == sales_outlet_id)]
#     peek_houres['hour'] = peek_houres['transaction_time'].dt.components.hours
#     peek_houres = peek_houres.groupby(['transaction_date', 'hour'])['hour'].count().reset_index(name='count')
#     max_hour_per_day = peek_houres.loc[peek_houres.groupby('transaction_date')['count'].idxmax()].reset_index(drop=True)
#     max_hour_per_day = max_hour_per_day.groupby('hour')['hour'].count().reset_index(name='count')
#     max_count_index = max_hour_per_day['count'].idxmax()
#     max_hour = max_hour_per_day.loc[max_count_index, 'hour']
#
#     return max_hour

def peak_hours(sales_outlet_id):
    houres_list = ['transaction_date', 'transaction_time', 'sales_outlet_id']
    filtered_df = sale_receipts_df[houres_list]
    filtered_df = filtered_df[filtered_df['sales_outlet_id'] == sales_outlet_id]
    filtered_df['hour'] = filtered_df['transaction_time'].dt.components.hours
    hourly_counts = filtered_df.groupby(['transaction_date', 'hour'])['hour'].count().reset_index(name='count')
    peak_hour_per_day = hourly_counts.loc[hourly_counts.groupby('transaction_date')['count'].idxmax()].reset_index(
        drop=True)

    # Count how often each hour was the peak across all days
    peak_hour_overall = peak_hour_per_day.groupby('hour')['hour'].count().reset_index(name='count')

    # Find the maximum count
    max_count = peak_hour_overall['count'].max()

    # Find all hours with the maximum count
    peak_hours = peak_hour_overall[peak_hour_overall['count'] == max_count]['hour'].tolist()

    return peak_hours


if __name__ == '__main__':
    peek = peak_hours(3)
    print(peek)
