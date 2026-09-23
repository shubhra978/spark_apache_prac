df = (spark.read
    .format("csv") #to read format as csv
    .option("header", "true") #if header present it will create headers for rows
    .option("inferSchema", "true") #will automatically select data type for each column
    .option("sep", ";") #to read separator
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/")) #to load the file from volume

df = df.repartition(2) #to repartition the data

#transformation-1
#narrow_transformation
df = df.select("Product ID", "Category")
df = df.filter(col("Category")=="Furniture")

#transformation-2
#wide_transformation
df = df.groupBy("Product ID").count()
display(df)
