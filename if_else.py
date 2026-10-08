from pyspark.sql.functions import *
from pyspark.sql.types import *

#import data

df_data = spark.read\
    .format("csv")\
    .option("header", "true")\
    .option("inferSchema", "true")\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/indian_roads_dataset.csv")
display(df_data.limit(50))


#applying if else and showing result on a new coolumn

df_ifelse = df_data\
    .withColumn("hourly_overview",\
        when(col("hour") < 12, "morning")\
        .when((col("hour") > 12) & (col("hour") < 18), "afternoon")\
        .otherwise("evening")\
    )
display(df_ifelse)
