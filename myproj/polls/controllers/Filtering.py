from .database import sale_receipts_df
import pandas as pd


class Filter:
    @staticmethod
    def filter_df(sales_outlet_id=None, start_date=None, end_date=None, filtering_list=None):
        filtered_df = sale_receipts_df[filtering_list]

        if sales_outlet_id:
            filtered_df = filtered_df[
                (filtered_df["sales_outlet_id"] == sales_outlet_id)
            ]

        if start_date and end_date:
            start_date = pd.to_datetime(start_date)
            end_date = pd.to_datetime(end_date)
            print(type(filtered_df["transaction_date"]))

            filtered_df["transaction_date"] = pd.to_datetime(filtered_df["transaction_date"])

            print(type(start_date))
            print(type(filtered_df["transaction_date"]))

            filtered_df = filtered_df[
                (filtered_df["transaction_date"] >= start_date) &
                (filtered_df["transaction_date"] <= end_date)
                ]
        return filtered_df

    @staticmethod
    def get_work_week_df(sales_df):
        sales_df = sales_df.assign(work_week=lambda x: x["transaction_date"].apply(lambda dt: dt.isocalendar()[1]))
        return sales_df

    @staticmethod
    def apply_total_sales(filtered_df):
        filtered_df = filtered_df.assign(total_sales=lambda x: (x['quantity'] * x['unit_price']))
        return filtered_df
