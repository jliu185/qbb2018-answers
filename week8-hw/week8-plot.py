#!/usr/bin/env python3

import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

filename = open(sys.argv[1])

per_list =[]

for i, line in enumerate(filename):
    fields = line.rstrip("\r\n").split("\t") 
    s_m = fields[3]
    e_m = fields[4]
    s_p = fields[10]
    e_p = fields[11]
    percentage = 100*(abs(float(s_m)-float(s_p))/abs(float(e_p)-float(s_p)))
    per_list.append(percentage)

fig, ax = plt.subplots()
plt.hist(per_list, bins=50)
plt.xlabel('Relative position of aligned frequencies')
plt.ylabel('counts/frequencies')
plt.title( 'Density plot where motif matches occur' )
plt.savefig('densityplot.png')
plt.close()

