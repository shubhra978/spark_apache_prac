from pyspark.sql.functions import*
from pyspark.sql.types import *

#read the file
df_ap = spark.read.\
    format("csv").\
        option("header", "true").\
        option("inferSchema", "true").\
        option("sep", ",").\
        load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/indian_roads_dataset.csv")
display(df_ap.limit(20))
