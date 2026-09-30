#renaming the column(will affect dataframe)
df_filter = df_filter.withColumnRenamed("city", "Targeted_City")
display(df_filter)


#multiplying and adding a new column
pinpoint_location = col("latitude")*col("longitude") 

df_filter_column_add = df_filter.withColumn("target_location", pinpoint_location)

display(df_filter_column_add.select(round("target_location",2))) 
