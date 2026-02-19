from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType

spark = SparkSession.builder \
    .appName("RealtimeShipmentStreamingPipeline") \
    .getOrCreate()

shipmentSchema = StructType() \
    .add("shipment_id", StringType()) \
    .add("origin", StringType()) \
    .add("destination", StringType()) \
    .add("transport_mode", StringType()) \
    .add("shipment_status", StringType()) \
    .add("weight_tons", IntegerType()) \
    .add("distance_km", IntegerType()) \
    .add("event_timestamp", StringType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "shipment_events") \
    .option("startingOffsets", "latest") \
    .load()

parsed = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), shipmentSchema).alias("data")) \
    .select("data.*")

query = parsed.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
