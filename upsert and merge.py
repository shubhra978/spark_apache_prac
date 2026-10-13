from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from delta.tables import DeltaTable

# 1. Initialize Spark with Delta Lake support
spark = SparkSession.builder \
    .appName("DeltaMergeAndLogExample") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

table_path = "/tmp/delta_customers"

# 2. Create Initial Target Table (Version 0)
initial_data = [
    (1, "Alice", "alice@example.com", 100),
    (2, "Bob", "bob@old.com", 200),
    (3, "Charlie", "charlie@example.com", 300)
]
initial_df = spark.createDataFrame(initial_data, ["id", "name", "email", "balance"])
initial_df.write.format("delta").mode("overwrite").save(table_path)

# 3. Prepare Incoming Source Data (Updates for Bob, New row for David)
incoming_data = [
    (2, "Bob", "bob@newdomain.com", 250),  # Matches id=2 -> Needs update
    (4, "David", "david@example.com", 400)   # Does not match -> Needs insert
]
source_df = spark.createDataFrame(incoming_data, ["id", "name", "email", "balance"])

# 4. Perform the MERGE (Upsert) Operation (Version 1)
target_table = DeltaTable.forPath(spark, table_path)

target_table.alias("target") \
    .merge(
        source_df.alias("source"),
        "target.id = source.id"
    ) \
    .whenMatchedUpdate(set={
        "email": col("source.email"),
        "balance": col("source.balance")
    }) \
    .whenNotMatchedInsert(values={
        "id": col("source.id"),
        "name": col("source.name"),
        "email": col("source.email"),
        "balance": col("source.balance")
    }) \
    .execute()

# Verify the final dataset
print("--- Current Table Data ---")
spark.read.format("delta").load(table_path).orderBy("id").show()
