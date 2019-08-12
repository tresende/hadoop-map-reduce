
from pyspark import SparkConf                                                                                                                 
from pyspark.context import SparkContext                                                                                                      
from pyspark.sql import SparkSession, SQLContext

from pyspark.sql import SparkSession

spark = SparkSession.builder \
     .appName("SparkonADF - Simple")\
     .enableHiveSupport()\
     .getOrCreate()


csvFile = spark.read.option("header", "true").csv("wasbs:///staging/capacity.csv")
csvFile = csvFile.where(csvFile.Year == 2015)
csvFile.write.mode("append").saveAsTable("capacity")


# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#      .appName("SparkonADF - Simple")\
#      .enableHiveSupport()\
#      .getOrCreate()

# from pyspark.sql.functions import *

# ## Read in HVAC file(s)


# df0 = spark.read.csv('wasbs://dticluster-hadoop-2019-06-08t14-14-23-717z@dtistoragea.blob.core.windows.net/HdiSamples/HdiSamples/SensorSampleData/hvac/HVAC.csv', header = True, inferSchema = True)

# ## Get Avg Temp by BuildingID
# df1 = df0.select(col('BuildingID'), col('ActualTemp')).groupBy('BuildingID').avg('ActualTemp')

# ## Write results to CSV file
# df1.repartition(1).write.csv('wasb://dticluster-hadoop-2019-06-08t14-14-23-717z@dtistoragea.blob.core.windows.net/output/AvgTempByDay', header = True, mode = 'overwrite')