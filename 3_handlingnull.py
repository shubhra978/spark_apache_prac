# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df_null = spark.read\
.format("csv")\
.option("header",True)\
.option("inferSchema",True)\
.load("/datasets/customers_raw.csv")
df_null = df_null.filter(col("customer_id").isNotNull())
df_null = df_null.filter(col("email").isNotNull())
# Display the final DataFrame using the display() function.
df_result =df_null
display(df_result)
