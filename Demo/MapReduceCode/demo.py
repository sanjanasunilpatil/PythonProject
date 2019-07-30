from pyspark import SparkContext
import sys
sc = SparkContext("local", "abc")
input = sc.textFile(sys.argv[1])
content = input.collect()
print(content)
