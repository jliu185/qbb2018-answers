#!/usr/bin/env python3

import sys
import pandas as pd

fxn = open(sys.argv[1])

# MORE PYTHONIC WAY OF DOING THE ABOVE EXAMPLE
for i, line in enumerate( fxn ):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t") 
    
    if fields[2] == '-':
        p_reg_e = int (fields[3]) + 500
        p_reg_s = int (fields[3])
        print(fields[1],p_reg_s,p_reg_e,fields[5])
    else:
        p_reg_s = int (fields[3]) - 500
        p_reg_e = int (fields[3])
        if p_reg_s < 0 :
            p_reg_s = 0
            print(fields[1],p_reg_s,p_reg_e,fields[5])




