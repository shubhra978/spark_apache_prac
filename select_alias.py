df_select = spark.read\
    .format("csv")\
        .option("header",True)\
            .option("inferSchema",True)\
                .option("sep", ";")\
                    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/Products.csv")
#using .alias to give new alias for a column
df_select.select(col("Category"),col("Product ID").alias("product_cat")).display()
