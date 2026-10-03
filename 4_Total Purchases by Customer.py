# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, asc
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

#Copy the starter code or load the file path available in the problem statement 
df_result = spark.read.format('csv')\
.option('header', True)\
.option('inferSchema',True)\
.load('/datasets/customer_purchases.csv')

df_result =df_result.groupBy("customer_id").agg(sum("purchase_amount").alias("total_purchase")).orderBy(asc("customer_id"))


# Display the final DataFrame using the display() function.
display(df_result)
