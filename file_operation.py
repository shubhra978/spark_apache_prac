df = spark.read\
    .format("csv")\
        .option("header", "true")\
        .option("inferSchema", "true")\
        .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/indian_roads_dataset.csv")


#overwrite
df.write\
    .format("csv")\
    .mode("overwrite")\
    .save("path","/Volumes/spark_job_stage_creation/spark_classes/spark_volume/demo_write_file/")

#append
df.write\
    .format("csv")\
    .mode("append")\
    .save("path","/Volumes/spark_job_stage_creation/spark_classes/spark_volume/demo_write_file/")

#ignore
df.write\
    .format("csv")\
    .mode("ignore")\
    .save("path","/Volumes/spark_job_stage_creation/spark_classes/spark_volume/demo_write_file/")

#error
df.write\
    .format("csv")\
    .mode("error")\
    .save("path","/Volumes/spark_job_stage_creation/spark_classes/spark_volume/demo_write_file/")
