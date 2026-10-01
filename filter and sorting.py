from pyspark.sql.functions import *
from pyspark.sql.types import *

df_filter = spark.read\
            .format("csv")\
                .option("inferSchema", "true")\
                .option("header", "true")\
                .option("delimiter", ",")\
                .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/indian_roads_dataset.csv")
display(df_filter.limit(10))

#selecting multiple filter from list
weekend_filter = ["Saturday", "Sunday"] 
df_filter = df_filter.filter(col("day_of_week").isin(weekend_filter))
display(df_filter)

#for having single filter
df_filter = df_filter.filter(col("day_of_week")=="Monday")
display(df_filter)


#sorting of data
df_csv = spark.read\
    .format("csv")\
        .option("header", True)\
            .option("sep", ",")\
                .option("inferSchema", True)\
                    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/indian_roads_dataset.csv")
#display(df_csv.limit(5))
display(df_csv.sort(col("accident_id").desc()).limit(5))
