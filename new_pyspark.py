from pyspark.sql import SparkSession
import pandas as pd
from . import something


# Basic case - direct conversion to pandas without exception conditions
def basic_conversion():
    spark = SparkSession.builder.appName("PySparkToPandasTest").getOrCreate()
    df = spark.read.csv("large_data.csv")
    pdf = df.toPandas()  # Noncompliant {{Consider using PySpark's built-in capabilities instead of converting this `DataFrame` to Pandas.}}
#         ^^^^^^^^^^^
    df.toPandas() # Noncompliant
