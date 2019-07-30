#!/opt/rh/rh-python36/root/usr/bin/python
from pyspark import SparkContext
import sys
sc = SparkContext("local", "abc")
input = sc.textFile(sys.argv[1])
words = input.collect()
print("Before foematting ",words)
dict_bygone_words = {}
for i in range(0, len(words), 1):
    if words[i].__contains__(' '):
        for split_word in words[i].split(' '):
            words.append(split_word)
        words.remove(words[i])
print("After formatting ", words)
for word in words:
    if word in dict_bygone_words.keys():
        dict_bygone_words[word] = int(dict_bygone_words[word] + 1)
    else:
        dict_bygone_words[word] = 1
print(dict_bygone_words)

