df_table = spark.read\
    .format("csv")\
        .option("header", "true")\
            .option("inferSchema", "true")\
                .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/indian_roads_dataset.csv")
display(df_table.limit(10))

#applying lit before each column while concatenating
df_concat = df_table.withColumn("date_time",concat(col("date"),lit("-"),col("time"),lit("-"),col("accident_id")))
#applying concat_ws for using lit once
df_concat_new = df_table.withColumn("date_time_new",concat_ws("-",col("date"),col("time"),col("accident_id")))
display(df_concat.limit(10))
