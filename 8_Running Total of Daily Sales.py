from pyspark.sql.window import Window
from pyspark.sql.functions import sum
w = Window.orderBy("order_date").rowsBetween(Window.unboundedPreceding,Window.currentRow) 
df_result = daily_sales.withColumn("running_total", sum("sales").over(w))
df_result.show()

#Calculate Total Sales and Average Order Value by Customer
from pyspark.sql.functions import sum, avg

df_result = orders.groupBy("customer_id")\
          .agg(sum("order_value").alias("total_sales")\
            ,avg("order_value").alias("avg_order_value"))  
df_result.show()
