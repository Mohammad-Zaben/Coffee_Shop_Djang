# from django.db import connection
#
# # Define your raw SQL query
# query = """
#             LOAD DATA INFILE 'C:/Users/Lenovo/Downloads/201904 sales reciepts.csv'
#             INTO TABLE polls_salesreceipts
#             FIELDS TERMINATED BY ','  -- Specify the delimiter, typically a comma for CSV files
#             ENCLOSED BY '"'           -- Specify if fields are enclosed by a character, typically double quotes
#             LINES TERMINATED BY '\n'  -- Specify the line terminator, typically a newline character
#             IGNORE 1 LINES            -- Skip the header row in the CSV file
# (transaction_id,transaction_date,transaction_time,instore_yn,customer_id,product_id,sales_outlet_id,line_item_amount,line_item_id,order,promo_item_yn,quantity,staff_id,unit_price)
# """
# # Execute the query
# with connection.cursor() as cursor:
#     cursor.execute(query)
#     results = cursor.fetchall()
#
# # Print the results
