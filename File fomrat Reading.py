#reading CSV
df_csv = spark.read\
    .format("csv")\
    .option("header", True)\
    .option("sep", ";")\
    .option("inferSchema",True)\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/Products.csv")

df_csv =df_csv.limit(5)
display(df_csv)
