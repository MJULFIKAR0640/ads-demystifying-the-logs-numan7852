#!/usr/bin/python

import sys

for line in sys.stdin:
    data = line.strip().split("/")
    if (len(data) > 1):
        print (data[2]).strip()
