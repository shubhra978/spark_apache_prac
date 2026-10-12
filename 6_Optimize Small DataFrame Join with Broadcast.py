from pyspark.sql.functions import broadcast

# customers(customer_id, region_code) and regions(region_code, region_name) are ready.
# TODO: join customers with regions on region_code (broadcast the small regions df),
#       keep customer_id and region_name, ordered by customer_id.

df_result = customers.join(broadcast(regions),"region_code","inner")   # replace this with your broadcast join
df_result = df_result.select("customer_id","region_name").orderBy("customer_id")
df_result.show()
