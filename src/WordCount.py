# -*- coding: utf-8 -*-
from pyspark import SparkContext, SparkConf
conf = SparkConf().setAppName("WordCount")
sc = SparkContext.getOrCreate();
contentRDD = sc.textFile("/user/cloudera/shakespeare.txt")
filter_empty_lines = contentRDD.filter(lambda x: len(x) > 0)
words = filter_empty_lines.flatMap(lambda x: x.split(' '))
wordcount = words.map(lambda x:(x,1)) \
    .reduceByKey(lambda x, y: x + y) \
    .map(lambda x: (x[1], x[0])).sortByKey(False)
wordcount.saveAsTextFile("/user/cloudera/shakespeare_clean")
