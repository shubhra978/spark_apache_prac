Salting is a procedure to remove skewness in dataframe while appling any kind of transformation.

from pyspark.sql.functions import *
from pyspark.sql.types import *

df_raw_data = [(1,'food'),(1,'food'),(1,'food'),(1,'food'),(1,'food'),(1,'food'),(2,'clothes'),(2,'clothes'),(2,'clothes'),(2,'clothes'),(2,'clothes'),(3,'shoes'),(3,'shoes'),(3,'shoes'),(3,'shoes')]

df_category = [(1,'mooncake'),(2,'shirts'),(3,'trousers')]

df_category = spark.createDataFrame(df_category, ['id', 'category'])

df_raw_data = spark.createDataFrame(df_raw_data, ['id', 'category'])


#with skewness
df_grouped_data = df_raw_data.groupBy('id').agg(count('category').alias('Cat_count'))


#applying salting by creating a salt column
df_salt_data = df_raw_data.withColumn('salt_col',floor(rand()*3))
df_salt_data = df_salt_data.withColumn('salt_together',concat(col('salt_col'),lit('-'),col('id')))
display(df_salt_data)

#applying group_by with salt column to remove skewness
df_grouped_data = df_salt_data.groupBy('salt_together').agg(count('category').alias('Cat_count'))
display(df_grouped_data)

#applying salting on category with array
df_category= df_category.withColumn("salt_id",array(*[lit(i) for i in range(3)]))
df_category = df_category.select('id','category',explode("salt_id").alias('salt_col'))
display(df_category)

#applying join with salted columns on both table
df = df_salt_data.join(df_category, (df_salt_data.id == df_category.id) & (df_salt_data.salt_col == df_category.salt_col),'left')
display(df)
