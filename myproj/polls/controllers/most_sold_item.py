from myproj.polls.controllers.Filtering import Filter


def filter_df():
    selling_list = ['product_id', 'quantity', 'sales_outlet_id']
    filtered_df = Filter.filter_df(filtering_list=selling_list)
    return filtered_df


def get_max_item(outlet_sales):
    outlet_sales['max_item'] = outlet_sales.groupby('product_id')['quantity'].transform('max')
    return outlet_sales


def get_quantity_df(most_selling_df):
    outlet_sales = most_selling_df.groupby(['product_id', 'sales_outlet_id'])['quantity'].sum().reset_index()
    return outlet_sales


def get_most_selling_item():
    most_selling_df = filter_df()
    outlet_sales = get_quantity_df(most_selling_df)
    outlet_sales = get_max_item(outlet_sales)
    most_selling_item = outlet_sales.loc[outlet_sales['quantity'].idxmax()]

    return (
        f"The most selling item is product ID {most_selling_item['product_id']}  "
        f"with  total quantity  {most_selling_item['quantity']}."
    )
