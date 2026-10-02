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


#using drop_na and assigning multiple columns containing null into a subset

# Initialize Spark session
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
spark = SparkSession.builder.appName('Spark Playground').getOrCreate()

df_null = spark.read\
.format("csv")\
.option("header",True)\
.option("inferSchema",True)\
.load("/datasets/customers_raw.csv")
subset=[col('customer_id'),col('email')]
df_null = df_null.dropna(subset=['customer_id','email']) #dropna function with subset for handling nulls for particular columns
# Display the final DataFrame using the display() function.
df_result =df_null
display(df_result)

#using drop_na with 'any' argument to just remove nulls from columns but doesnot work as full null rows
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
df_null = df_null.dropna('any')
# Display the final DataFrame using the display() function.
df_result =df_null
display(df_result)



