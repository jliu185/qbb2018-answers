#!/usr/bin/env python

"""
./manhattan.py plink.#.qassocc P#_Manhattan_plot
"""

import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

qassoc = open(sys.argv[1])
name = str(sys.argv[2])

p_xsig = []
p_xnonsig = []
p_ysig = []
p_ynonsig = []
count = 0

for line in qassoc:
    if "SNP" in line or "NA" in line:
        pass
    else: 
        count += 1
        line = line.rstrip('\r\n').split()
        p_val = -np.log(float(line[8]))
        cutoff = -np.log(10e-5)
        if p_val > cutoff:
            p_xsig.append(count)
            p_ysig.append(p_val)
        else: 
            p_xnonsig.append(count)
            p_ynonsig.append(p_val)


#plotting the manhattan plot
plt.figure()
plt.scatter(p_xsig,p_ysig, alpha=.6, color = "red", s = 5, label = "p>10e-5")
plt.scatter(p_xnonsig,p_ynonsig, alpha=.6, color = "blue", s = 5, label = "p<10e-5")
plt.xlabel("Gene position")
plt.ylabel("-log10(p-value)")
plt.title(name)
plt.legend()
plt.savefig('graphs/P46_manhattan_plot.png')
plt.close()