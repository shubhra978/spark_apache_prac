from pyspark.sql.functions import *

result = (
    sales_data.groupBy("product")
    .agg( #agg function is used to calculate multiple aggregation
        sum("quantity").alias("total_qty"), #calculating sum of quantity and changing output column name
        sum(when(col("region") == "West", col("quantity")).otherwise(0)).alias("west_qty"), #using case when with sum to calculate on filter
        countDistinct("region").alias("region_count"), #countng distinct values
        count("order_id").alias("order_count")
    )
    .orderBy(col("product").asc())
)

result.show()
