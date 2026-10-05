# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum,col
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#product table

products = spark.createDataFrame([
    (1, "Apple Juice",        "Beverages"),
    (2, "Orange Juice",       "Beverages"),
    (3, "Chocolate Bar",      "Snacks"),
    (4, "Potato Chips",       "Snacks"),
    (5, "Fresh Strawberries", "Fruits"),
    (6, "Sparkling Water",    "Beverages"),
], ["product_id", "name", "category"])

#sales table

sales = spark.createDataFrame([
    (1, 1, 10, 20),
    (2, 1,  5, 10),
    (3, 2,  8, 16),
    (4, 3,  2,  4),
    (5, 4, 15, 30),
    (6, 4,  5, 10),
    (7, 6, 12, 24),
], ["sale_id", "product_id", "quantity", "revenue"])

#inventory table

inventory = spark.createDataFrame([
    (1, 50, "Warehouse A"),
    (2, 40, "Warehouse A"),
    (2, 20, "Warehouse B"),
    (3, 30, "Warehouse A"),
    (4, 20, "Warehouse A"),
    (4, 15, "Warehouse B"),
    (5, 10, "Warehouse A"),
], ["product_id", "stock", "warehouse"])
#, "name", "category", "sale_id", #, "quantity", "revenue",#, "stock", "warehouse"
#Copy the starter code or load the file path available in the problem statement 
#Aggregate sales: For each product, compute total_quantity and total_revenue by summing across all sales rows.
agg_sales = sales\
.groupBy("product_id")\
.agg(sum("quantity").alias("total_quantity"),\
     sum("revenue").alias("total_revenue")\
    )
#Aggregate inventory: For each product, compute total_stock by summing stock across all warehouses.
agg_inventory = inventory\
.groupBy("product_id")\
.agg(sum("stock").alias("total_stock")\
    )

#Combine: Join the aggregated sales and inventory data with the products table so every product appears in the output.
df_combine = products\
.join(agg_sales,"product_id","left")\
.join(agg_inventory,"product_id","left")

#Combine: Join the aggregated sales and inventory data with the products table so every product appears in the output.
df_combine=df_combine\
.orderBy("product_id",ascending= True)\
.fillna(0)
#retain original types of column
result = df_combine\
.withColumn("total_quantity", col("total_quantity").cast("long"))\
.withColumn("total_revenue", col("total_revenue").cast("long"))\
.withColumn("total_stock", col("total_stock").cast("long"))

display(result)
