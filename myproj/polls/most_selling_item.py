import pandas as pd
import plotly.express as px
from .database import sale_receipts_df


def selling_item_plot(most_sales_product):
    fig = px.scatter(most_sales_product,
                     x='product_id',
                     y='quantity',
                     color='sales_outlet_id',
                     symbol='sales_outlet_id',
                     title='Most Selling Item for Each Store',
                     labels={'product_id': 'Product ID', 'quantity': 'Total Quantity Sold'},
                     hover_data={'product_id': True, 'quantity': True, 'sales_outlet_id': True})
    fig.show()


def selling_item():
    selling_list = ['product_id', 'quantity', 'sales_outlet_id']
    filtered_sales_df = sale_receipts_df[selling_list]
    outlet_sales = filtered_sales_df.groupby(['product_id', 'sales_outlet_id'])['quantity'].sum().reset_index()
    outlet_sales['max_item'] = outlet_sales.groupby('product_id')['quantity'].transform('max')
    most_sales_product = outlet_sales[outlet_sales['quantity'] == outlet_sales['max_item']]
    most_selling_item = most_sales_product.loc[most_sales_product['quantity'].idxmax()]
    return (
        f"The most selling item is product ID {most_selling_item['product_id']} in the outlet id :{most_selling_item['sales_outlet_id']} with a total quantity of {most_selling_item['quantity']}.")

    # here call selling_item_plot function
    selling_item_plot(most_sales_product)


if __name__ == '__main__':
    selling_item()
