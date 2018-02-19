import socket
import threading
import os
import sys

# This example uses the older Streaming API

from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext

# conf = (SparkConf()
#          .setMaster("spark://192.168.1.33:7077")
#          .setAppName("PythonStreamingExample"))

# sc = SparkContext(conf = conf)

sc = SparkContext(appName="PythonStreamingNetworkWordCount2")
ssc = StreamingContext(sc, 1) # second argument is the batch interval in seconds.

# 9999 1MB text file
# 9998 tiny text file
# 9997 nc with stdin

lines = ssc.socketTextStream('192.168.1.3', 9999)

lines.flatMap(lambda line: line.split(" "))\
              .map(lambda word: (word, 1))\
              .reduceByKey(lambda a, b: a+b).pprint()

ssc.start()
ssc.awaitTermination()