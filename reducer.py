#!/usr/bin/env python

import sys
from operator import itemgetter

prv_key = None
item_values = []

for line in sys.stdin:
    curnt_key, idx, value = line.rstrip().split("\t")
    idx, value = map(int,[idx,value])
    if curnt_key == prv_key:
        item_values.append((idx,value))
    else:
        if prv_key:
            item_values = sorted(item_values,key=itemgetter(0))
            i = 0
            result = 0
            while i < len(item_values) - 1:
                if item_values[i][0] == item_values[i + 1][0]:
                    result += item_values[i][1]*item_values[i + 1][1]
                    i += 2
                else:
                    i += 1
            print "%s,%s"%(prv_key,str(result))
        prv_key = curnt_key
        item_values = [(idx,value)]

if curnt_key == prv_key:
    item_values = sorted(item_values,key=itemgetter(0))
    i = 0
    result = 0
    while i < len(item_values) - 1:
        if item_values[i][0] == item_values[i + 1][0]:
            result += item_values[i][1]*item_values[i + 1][1]
            i += 2
        else:
            i += 1
    print "%s,%s"%(prv_key,str(result))




