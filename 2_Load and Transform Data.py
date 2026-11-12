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
#filter as per requirement
df = df.filter((col("purchase_amount")>100) & (col("age")>=30))

df_result = df.select("customer_id","name", "purchase_amount")
# Display the final DataFrame using the display() function.
display(df_result)



Count Rows per City
from pyspark.sql.functions import *

employees = employees.groupby('city').agg(count('name').alias('count'))
df_result = employees.orderBy('city')  # TODO: groupBy city, count, order by city
df_result.show()
