#Inner Join Orders with Customers

from pyspark.sql.functions import *
from pyspark.sql.types import *
df_result  = customers.join(orders, on = 'customer_id', how = 'inner')
df_result = df_result.select('customer_id','order_id','amount','name')
 # TODO: join with customers on customer_id
df_result.show()


#Orders: List Orders With Customer Names (INNER JOIN)

from pyspark.sql.functions import *
from pyspark.sql.types import *

df_all = customers.join(\
orders\
on = 'customer_id'\
, how = 'inner')
df_all  = df_all.select('order_id','order_date','customer_name')
display(df_all)
