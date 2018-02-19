To run:

0. Download Apache Spark and unzip on local machine.

1. Setup port forwarding to Spark Master Host (e.g.):
```
ssh -L 8080:localhost:8080 -L 8888:localhost:8888 -L 7077:192.168.1.33:7077 spark-prod
```

2. Deploy:
```
./pi_example.sh
```

3. Look at Job status:
```
http://localhost:4040
```


./bin/spark-submit --class org.apache.spark.examples.SparkPi --master spark://192.168.1.33:7077 ~/spark-2.2.1-bin-hadoop2.7/examples/jars/spark-examples_2.11-2.2.1.jar 1000