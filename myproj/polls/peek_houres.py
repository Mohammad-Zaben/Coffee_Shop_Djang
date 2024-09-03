from matplotlib import pyplot as plt

from .database import sale_receipts_df
import seaborn as sns


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


def peek_houres(sales_outlet_id):
    houres_list = ['transaction_date', 'transaction_time', 'sales_outlet_id']
    peek_houres = sale_receipts_df[houres_list]
    peek_houres = peek_houres[(peek_houres["sales_outlet_id"] == sales_outlet_id)]
    peek_houres['hour'] = peek_houres['transaction_time'].apply(lambda x: x.seconds // 3600)
    peek_houres = peek_houres.groupby(['transaction_date', 'hour'])['hour'].count().reset_index(name='count')
    max_hour_per_day = peek_houres.loc[peek_houres.groupby('transaction_date')['count'].idxmax()].reset_index(drop=True)
    max_hour_per_day = max_hour_per_day.groupby('hour')['hour'].count().reset_index(name='count')
    print(max_hour_per_day)
    # Plot the sales scatter plot
    # sales_scatter_plot(max_hour_per_day)
    max_count_index = max_hour_per_day['count'].idxmax()
    # Get the corresponding hour
    max_hour = max_hour_per_day.loc[max_count_index, 'hour']

    return max_hour


if __name__ == '__main__':
    peek = peek_houres(3)
    print(peek)
