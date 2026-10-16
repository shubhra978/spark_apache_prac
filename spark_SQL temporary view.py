#we can create a temporary view where we can use sql commands for transformation


# Create a temporary SQL view from the DataFrame
df_new.createOrReplaceTempView("df_new")

# Run Spark SQL and store the result in a new DataFrame
severe_high_traffic_by_city = spark.sql("""
    SELECT
        city,
        COUNT(*) AS accident_count
    FROM df_new
    WHERE accident_severity = 'Severe'
      AND traffic_density = 'High'
    GROUP BY city
""")

# Display the result in Databricks
display(severe_high_traffic_by_city)
