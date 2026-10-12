from pyspark.sql.functions import *
from pyspark.sql.types import *

@udf(returnType = StringType()) #converting the value of return type to string
def get_date_time(date,time):
  return str(date) + ' ' + str(time)
#creating a new data frame and calling the udf function defined 
data = [(1, '2022-01-01', '10:00:00'), (2, '2022-01-02', '11:00:00'), (3, '2022-01-03', '12:00:00'), (4, '2022-01-04', '13:00:00')] #creating data from scratech in a list format
df = spark.createDataFrame(data, ['accident_id', 'date', 'time']) #creating dataframe with column names
df = df.withColumn('date_time', get_date_time(df.date, df.time)) #calling the udf funciton 
display(df)
