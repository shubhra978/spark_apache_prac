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

#pyspark_Sql using spark.sql
df_ap.createOrReplaceTempView("df_sql")
df_sql = spark.sql("""
                   select 
                   city,
                   array_agg(temperature),
                   collect_list(temperature),
                    collect_set(temperature),
                    min(temperature),
                    max(temperature),
                    avg(temperature),
                    mode(temperature)
                    from df_sql
                    group by city
                   """)
display(df_sql)

#using only sql
%sql
select city,
array_agg(temperature),
collect_list(temperature),
collect_set(temperature),
min(temperature),
max(temperature),
avg(temperature),
mode(temperature)
 from df_sql
 group by city
 order by city


df_ap = df_ap.groupBy("city").agg(collect_list("temperature").alias("array_agg(temperature)"),\
     count("temperature").alias("count(temperature)"),\
          avg("temperature").alias("avg(temperature)"),\
               sum("temperature").alias("sum(temperature)"),\
                    max("temperature").alias("max(temperature)"),\
                         min("temperature").alias("min(temperature)"),\
                             array_agg("temperature").alias("array_agg(temperature)"),\
                                 collect_set("temperature").alias("collect_set(temperature)"))
display(df_ap)
