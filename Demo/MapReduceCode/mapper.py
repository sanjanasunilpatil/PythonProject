#!/opt/rh/rh-python36/root/usr/bin/python
import sys

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        print(word,'1',sep='\t')
