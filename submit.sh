#!/usr/bin/env bash

# Deploy mode:
# cluster: run remotely, report back console output
# client: relay everything, run it locally.
# Note: 'cluster' deploy mode not supported for Python: https://spark.apache.org/docs/latest/submitting-applications.html


SPARK_HOME=~/spark-2.2.1-bin-hadoop2.7

$SPARK_HOME/bin/spark-submit \
    --master spark://localhost:7077 \
    --deploy-mode client \
    --verbose \
    --supervise \
    $SPARK_HOME/examples/src/main/python/pi.py 5
#    pi_example.py

#    --master local[1] \
