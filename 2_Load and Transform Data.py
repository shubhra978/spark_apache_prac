# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df =spark.read\
      .format("csv")\
      .option("header",True)\
      .option("inferSchema",True)\
      .load("/datasets/customers.csv")
df = df.filter((col("purchase_amount")>100) & (col("age")>=30))

df_result = df.select("customer_id","name", "purchase_amount")
# Display the final DataFrame using the display() function.
display(df_result)
