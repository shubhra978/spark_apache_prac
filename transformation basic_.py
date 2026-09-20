#transformation - 1
df_select = df.select('id','gender','age','salary')
df_select.display()

#transformation - 2
df_filter = df.filter((col("id")>5) & (col("age")>35))
#display in table_row format
df_filter.display()
#display in old sql table format
df_filter.show()

#casting of columns into proper type manually
df.withColumn("salary",col("salary").cast("int"))
df.withColumn("age",col("age").cast("int"))
df.withColumn("id",col("id").cast("int"))
#printing the types of each schema
df.printSchema()
#displaying the types of each schema
print(df.dtypes)
