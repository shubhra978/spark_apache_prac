from pyspark.sql.window import Window
from pyspark.sql.functions import sum
w = Window.orderBy("order_date").rowsBetween(Window.unboundedPreceding,Window.currentRow) 
df_result = daily_sales.withColumn("running_total", sum("sales").over(w))
df_result.show()
