df_old_module = spark.read\
    .format("csv")\
    .option("header",True)\
    .option("inferSchema",True)\ #default creation of schema by pyspark with inferschema command
    .option("sep",";")\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/Products.csv")

df_old_module = df_old_module.limit(5)
display(df_old_module)


#enforcing a new schema on a table to change the types of the column
#procedure used = Enforced Schema

my_new_schema = StructType([StructField('Product ID', IntegerType(), True),\
     StructField('Category', IntegerType(), True),\
          StructField('Sub-Category', StringType(), True),\
               StructField('Product Name', StringType(), True)])

df_enforced_module = spark.read\
    .format("csv")\
    .option("header",True)\
    .option("sep",";")\
    .schema(my_new_schema)\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/Products.csv")

df_enforced_module = df_enforced_module.limit(5)
display(df_enforced_module)
df_enforced_module.schema
df_enforced_module.printSchema()

#defining a new schema on a table to change the types of the column like DDL statement in SQL
#procedure used = DDL Schema 

my_ddl_schema = """
`Product ID` STRING,
`Category` STRING,
`Sub-Category` STRING,
`Product Name` STRING
"""

df_ddl_module = spark.read\
    .format("csv")\
    .option("header",True)\
    .option("sep",";")\
    .schema(my_ddl_schema)\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/Products.csv")

df_ddl_module = df_ddl_module.limit(5)
display(df_ddl_module)
df_ddl_module.schema


#prinitng of all schema
df_enforced_module.printSchema()
df_ddl_module.printSchema()
df_old_module.printSchema()

root
 |-- Product ID: integer (nullable = true)
 |-- Category: integer (nullable = true)
 |-- Sub-Category: string (nullable = true)
 |-- Product Name: string (nullable = true)

root
 |-- Product ID: string (nullable = true)
 |-- Category: string (nullable = true)
 |-- Sub-Category: string (nullable = true)
 |-- Product Name: string (nullable = true)

root
 |-- Product ID: string (nullable = true)
 |-- Category: string (nullable = true)
 |-- Sub-Category: string (nullable = true)
 |-- Product Name: string (nullable = true)


