# sales DataFrame: order_id, customer_id, product_id, amount, order_date

# TODO: count orders per customer per month (month = first day of month)
from pyspark.sql.functions import *
from pyspark.sql.types import *
sales = sales \
    .withColumn('Month', trunc('order_date', 'month')) \
    .groupBy('customer_id', 'Month') \
    .agg(F.count('order_id').alias('Order_count'))
result = sales.select('customer_id','month','order_count')
result.show()
