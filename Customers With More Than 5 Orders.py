# sales DataFrame: order_id, customer_id, product_id, amount, order_date
from pyspark.sql.functions import *
# TODO: customers who placed MORE THAN 5 orders

result = sales.groupBy("customer_id").agg(count("order_id").alias("Order_count"))
result = result.select(col("Customer_id")).filter(col("Order_count") > 5)
result.show()
