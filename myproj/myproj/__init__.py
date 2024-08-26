from django.db import connection

# Define your raw SQL query
query = """
    LOAD DATA INFILE 'C:/Users/Lenovo/Downloads/201904 sales reciepts.csv'
    INTO TABLE polls_salesreceipts
    FIELDS TERMINATED BY ','
    ENCLOSED BY '"'
    LINES TERMINATED BY '\n'
    IGNORE 1 LINES
    (transaction_id, transaction_date, transaction_time, sales_outlet_id, staff_id, customer_id, instore_yn, `order`, line_item_id, product_id, quantity, line_item_amount, unit_price, promo_item_yn);
"""

# Execute the query
with connection.cursor() as cursor:
    cursor.execute(query)
    # If you're not fetching results, you don't need to use fetchall()
    # Remove the line below if no results are expected
    results = cursor.fetchall()

# Print the results (if needed)
print(results)
