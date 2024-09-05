import pandas as pd
import threading

# Sample data

def extract_data():
    data = {
        'customer_id': [1, 2, 1, 3, 2, 3, 1],
        'store': ['A', 'A', 'B', 'B', 'A', 'B', 'A'],
        'price': [100, 200, 150, 300, 100, 250, 200],
        'quantity': [1, 2, 3, 4, 5, 6, 7],
        'date': pd.to_datetime(['2024-08-01', '2024-08-02', '2024-08-03', '2024-08-04', '2024-08-05', '2024-08-06', '2024-08-07'])
    }

    return pd.DataFrame(data)

# Model: Handles the data processing
class SalesDataModel:
    def _init_(self, data):
        self.df = pd.DataFrame(data)

    @staticmethod
    def get_filtered_df(start_date, end_date):
        return df[(df['date'] >= start_date) & (df['date'] <= end_date)]

    @staticmethod
    def get_total_sales(price, quantity):
        return price * quantity

    def apply_total_sales(self):
        self.df['total_sales'] = self.df.apply(lambda row: self.get_total_sales(row['price'], row['quantity']), axis=1)

# View: Handles the display of results
class SalesDataView:
    @staticmethod
    def display(data):
        print(data)

# Controller: Handles the application logic and threading
class SalesDataController:
    def _init_(self, model, view):
        self.model = model
        self.view = view

    def get_sales(self, start_date, end_date, store=None, customer_id=None):
        self.model.apply_total_sales()
        filtered_df = self.model.get_filtered_df(start_date, end_date)

        if customer_id and store:
            grouped_sales_store = filtered_df.groupby(['customer_id', 'store'])['total_sales'].sum().reset_index()
            self.view.display(grouped_sales_store)
        elif customer_id:
            grouped_sales = filtered_df.groupby('customer_id')['total_sales'].sum().reset_index()
            self.view.display(grouped_sales)
        elif store:
            grouped_sales = filtered_df.groupby('store')['total_sales'].sum().reset_index()
            self.view.display(grouped_sales)


    def get_receipts(self, start_date, end_date, store=None, customer_id=None):
        # TODO impelment receipts logic
        pass


    def get_bla_bla(self):
        #         TODO implement bla bla logic
        pass

def upload_data(data):
    # TODO implement upload data logic
    print(data)
    # def execute_function_in_thread(self, func, *args):
    #     thread = threading.Thread(target=func, args=args)
    #     thread.start()
    #     return thread

# Instantiate the model, view, and controller

if __name__ == '__main__':


    # define flow
    data = extract_data()
    model = SalesDataModel(data)
    view = SalesDataView()
    controller = SalesDataController(model, view)

# Example: Running get_sales in a thread
# thread_sales = controller.execute_function_in_thread(controller.get_sales, '2024-08-02', '2024-08-05', customer_id=True)
# thread_sales.join()  # Wait for the thread to finish