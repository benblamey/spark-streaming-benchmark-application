import time
from pyspark import SparkConf, SparkContext
from pyspark.streaming import StreamingContext
from haste.benchmarking.messaging import parse_message

sc = SparkContext(appName="StreamingBenchmark")
ssc = StreamingContext(sc, 1)  # second argument is the batch interval in seconds.

# Port for Streaming Server is 9999
# IP address that worker node will connect to (don't use localhost or 127.0.0.1)
#lines = ssc.socketTextStream('192.168.1.33', 9999)  # LovisaInstance
lines = ssc.socketTextStream('localhost', 9999)  # LovisaInstance


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
