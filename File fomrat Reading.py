#reading CSV
df_csv = spark.read\
    .format("csv")\
    .option("header", True)\
    .option("sep", ";")\
    .option("inferSchema",True)\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/Products.csv")

df_csv =df_csv.limit(5)
display(df_csv)

#json reading
df_json = spark.read\
    .format("JSON")\
    .option("multiline", True)\
    .option("inferSchema", True)\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/airports.json")
df_json =df_json.limit(10)
import pyspark.sql.functions as F
# 1. Read as text file
df_text = spark.read.text("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/airports.json")
# 2. Extract the JSON part using regex (removes everything up to the first '{')
df_cleaned = df_text.select(F.regexp_extract("value", "(\\{.*)", 1).alias("json_str"))
# 3. Parse the cleaned string as JSON
df_final = df_cleaned.select(F.from_json("json_str", "city STRING, code STRING, country STRING, lat DOUBLE, lon DOUBLE, name STRING").alias("data")).select("data.*")
display(df_final.limit(10))

#parquet reading
df_parquet = spark.read\
    .format("parquet")\
    .load("/Volumes/spark_job_stage_creation/spark_classes/spark_volume/titanic.parquet")
display(df_parquet.limit(10))

#defining the url in a separate variable
myurl = "jdbc:postgresql://spark-job-stage-postgresql.postgres.database.azure.com:5432/spark_job_stage_postgresql?user=spark_job_stage_postgresql%40spark-job-stage-postgresql&password=Sparkjobstage123456789&ssl=true&sslfactory=org.postgresql.ssl.NonValidatingFactory"

#defining the connection user and pass separately for calling
connection = {
    "user" : "postgres",
    "password" : "Sparkjobstage123456789",
    "driver" : "org.postgresql.Driver"
}
#reading jdbc files
df_jdbc = spark.read.jdbc(url=myurl, table="airports",properties=connection)
display(df_jdbc.limit(10))


