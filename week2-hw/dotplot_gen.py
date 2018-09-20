#!/usr/bin/env python

"""
Usage:
./dotplot_gen.py <sorted lastz out file> <name of desired png file>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np

lastz = open(sys.argv[1])

xcount = 0
ycount = 0
plt.figure()
for line in lastz:
    xcount += 1
    if xcount == 1:
        continue
    else:
        line = line.rstrip('\r\n').split('\t')
        start,stop = int(line[0]),int(line[1])
        plt.plot([start, stop], [ycount, ycount + abs(stop-start)])
        ycount += abs(stop - start)

plt.xlim(0, 100000)
plt.ylim(0, 90000)
plt.xlabel('ref pos')
plt.ylabel('contig pos')
plt.title(sys.argv[2])
plt.savefig(str(sys.argv[2]) + ".png")
plt.close()