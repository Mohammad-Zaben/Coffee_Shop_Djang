from myproj.polls.controllers.database import sale_receipts_df


class Filter:
    @staticmethod
    def filter_df(sales_outlet_id=None, start_date=None, end_date=None, filtering_list=None):
        filtered_df = sale_receipts_df[filtering_list]

        if sales_outlet_id:
            filtered_df = filtered_df[
                (filtered_df["sales_outlet_id"] == sales_outlet_id)
                ]
        if start_date and end_date:
            filtered_df = filtered_df[
                (filtered_df["transaction_date"] >= start_date) &
                (filtered_df["transaction_date"] <= end_date)
                ]

        return filtered_df
