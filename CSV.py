from pyspark import SparkContext
import pyspark
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
#from pyspark import SparkContext
df = spark.read.format("csv").load("/Users/shanshajahan/Downloads/annual-enterprise-survey-2020-financial-year-provisional-csv.csv",
                                   header='true')

df.show(2)
#df.count()