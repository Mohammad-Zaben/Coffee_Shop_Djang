from sqlalchemy import create_engine
import pandas as pd


engine = create_engine('mysql+pymysql://root:@localhost:3306/test_data')
sale_receipts_df = pd.read_sql('SELECT * FROM salereciepts', con=engine)

# Convert the 'transaction_date' column to datetime format
sale_receipts_df['transaction_date'] = pd.to_datetime(sale_receipts_df['transaction_date'])

# def selling_item():
#   selling_list=['product_id' ,'quantity' ,'sales_outlet_id']
#   filtered_sales_df = sale_receipts_df[selling_list]
#   most_selling=filtered_sales_df.groupby(['sales_outlet_id' ,'product_id']) ['quantity'].count().reset_index(name='count')
#   most_selling_item = most_selling.loc[most_selling['count' ].idxmax()]
#  # print(most_selling)
#   print(most_selling_item)

# def selling_item():
#     selling_list = ['product_id', 'quantity', 'sales_outlet_id']
#     filtered_sales_df = sale_receipts_df[selling_list]
#
#     # Group by product_id and sum the quantities across all outlets
#     most_selling = filtered_sales_df.groupby('product_id')['quantity'].sum().reset_index(name='total_quantity')
#
#     # Find the product with the highest total quantity sold across all outlets
#     most_selling_item = most_selling.loc[most_selling['total_quantity'].idxmax()]
#
#     # Print the most selling item
#     print(f"The most selling item across all outlets is product ID {most_selling_item['product_id']} with a total quantity of {most_selling_item['total_quantity']}.")

def selling_item():
    selling_list = ['product_id', 'quantity', 'sales_outlet_id']
    filtered_sales_df = sale_receipts_df[selling_list]
    outlet_sales = filtered_sales_df.groupby(['product_id', 'sales_outlet_id'])['quantity'].sum().reset_index()
    #This means that we are looking for the maximum value in the quantity column for each product.For a product with product_id 1, the quantities are 10, 15, and 12. The maximum value is 15
    outlet_sales['max_item'] = outlet_sales.groupby('product_id')['quantity'].transform('max')

    most_sales_product = outlet_sales[outlet_sales['quantity'] == outlet_sales['max_item']]
    most_selling_item = most_sales_product.loc[most_sales_product['quantity'].idxmax()]
    print(f"The most selling item is product ID {most_selling_item['product_id']} in the outlet id :{most_selling_item['sales_outlet_id']} with a total quantity of {most_selling_item['quantity']}.")


if __name__ == '__main__':
      selling_item()