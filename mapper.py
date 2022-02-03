#!/usr/bin/env python

import sys
r_m = 2
c_n = 2 
line_index=0

for line in sys.stdin:
    row_values = map(int,line.split())
	if line_index < r_m:
        for j in range(0, len(row_values)):
			for k in range(0, c_n): 
                key = str(line_index) + "," + str(k)
                print "%s\t%s\t%s"%(key,j,row_values[j])
	else:
        for j in range(0, len(row_values)):
			for k in range(0, r_m): 
                key =  str(k)  + "," + str(j)
                print "%s\t%s\t%s"%(key,str(line_index-r_m),row_values[j])
    line_index = line_index + 1

