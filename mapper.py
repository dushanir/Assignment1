#!/usr/bin/env python

import sys
row_a = 2
col_b = 2 

for line in sys.stdin:
	matrix_index=0
    row_values = map(int,line.split())
	if matrix_index < row_a:
        for j in range(0, len(row_values)):
			for k in range(0, col_b): 
                key = str(matrix_index) + "," + str(k)
                print "%s\t%s\t%s"%(key,j,row_values[j])
	else:
        for j in range(0, len(row_values)):
			for k in range(0, row_a): 
                key =  str(k)  + "," + str(j)
                print "%s\t%s\t%s"%(key,str(matrix_index-row_a),row_values[j])
    matrix_index = matrix_index + 1
