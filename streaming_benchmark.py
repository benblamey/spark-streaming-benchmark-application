import time

import os
os.environ['PYSPARK_PYTHON'] = 'python3'

from pyspark import SparkContext
from pyspark.streaming import StreamingContext



sc = SparkContext(appName="StreamingBenchmark")
ssc = StreamingContext(sc, 1)  # second argument is the batch interval in seconds.


# Self-contained - so that it can be submitted as a single script (no external deps. ex. Spark)

# Port for Streaming Server is 9999
# IP address that worker node will connect to (don't use localhost or 127.0.0.1 in a cluster context)
lines = ssc.socketTextStream('192.168.1.13', 9999)  # LovisaInstance
#lines = ssc.socketTextStream('localhost', 9999)


# Copied from messaging.py
def parse_message(line):
    return {'cpu_pause_ms': int(line[1:7])}

def process_line(line):
    parsed = parse_message(line)
    sleep_ms = parsed['cpu_pause_ms']
    sleep_s = sleep_ms / 1000
    # Should do some work instead to keep the core busy
    # Spark tracks the cores so think its OK
    time.sleep(sleep_s)


lines.map(lambda line: process_line(line)).count().pprint()

ssc.start()
ssc.awaitTermination()
