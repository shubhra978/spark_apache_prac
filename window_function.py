#importing sql function for executing sql commands
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql.window import Window
#creating values as required
data = [
    (1,'James','Smith',36, 'M', 60000),
    (2,'Michael','Rose', 41,'M',70000),
    (3,'Robert','Williams', 36,'M',65000),
    (4,'Maria','Jones', 55,'F',80000),
    (5,'Jen','Brown', 30,'F',75000),
    (6,'Sara','Davis', 45,'F',90000),
    (7,'Tom','Miller', 45,'M',85000),
    (8,'Alice','Garcia', 25,'F',65000),
    (9,'Bob','Lopez', 32,'M',70000),
    (10,'Charlie','Hernandez', 40,'M',75000),
    (11,'David','Perez', 38,'M',80000),
    (12,'Ella','Rodriguez', 55,'F',60000),
    (13,'Fiona','Gonzalez', 35,'F',70000)
]
#creating the column heads
columns = ['id','firstname','lastname','age','gender','salary']
#creating a data frame to make a strcuture of a table
df_table = spark.createDataFrame(data, columns)
display(df_table)

#window functions at a glance
df_window = df_table\
#adding row number
.withColumn('row_number', row_number().over(Window.orderBy('age')))\
#adding rank function
    .withColumn('rank',rank().over(Window.partitionBy('age').orderBy('salary')))\
#adding denserank function
        .withColumn('dense_rank',dense_rank().over(Window.partitionBy('age').orderBy('salary')))\
#adding cumulative sum function using row preceding 
        .withColumn('cumulative_sum',sum('salary').over(Window.orderBy('salary').rowsBetween(Window.unboundedPreceding,Window.currentRow)))
display(df_window)
