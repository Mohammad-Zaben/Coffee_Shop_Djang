# from django.db import connection
#
# # Disable foreign key checks
# with connection.cursor() as cursor:
#     cursor.execute("SET FOREIGN_KEY_CHECKS=0;")
#
#     # Your LOAD DATA INFILE query
#     query = """
#         LOAD DATA INFILE 'C:/Users/Lenovo/Downloads/201904 sales reciepts.csv'
#         INTO TABLE polls_salesreceipts
#         FIELDS TERMINATED BY ','
#         ENCLOSED BY '"'
#         LINES TERMINATED BY '\n'
#         IGNORE 1 LINES
#         (`transaction_id`, `transaction_date`, `transaction_time`, `staff_id`, `instore_yn`, `order`,
#          `line_item_id`, `quantity`, `line_item_amount`, `unit_price`, `promo_item_yn`,
#          `customer_id`, `product_id`, `sales_outlet_id`)
#     """
#     cursor.execute(query)
#
#     # Re-enable foreign key checks
#     cursor.execute("SET FOREIGN_KEY_CHECKS=1;")
