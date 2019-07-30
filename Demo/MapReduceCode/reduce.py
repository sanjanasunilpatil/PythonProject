#!/opt/rh/rh-python36/root/usr/bin/python
import sys

dict_bygone_words = {}
for line in sys.stdin:
    line = line.strip()
    words = line.split('\t')
    if words[0] not in dict_bygone_words.keys():
        dict_bygone_words[words[0]] = words[1]
    else:
        dict_bygone_words[words[0]] = int(dict_bygone_words[words[0]]) + 1

print(dict_bygone_words)
