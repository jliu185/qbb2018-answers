#!/usr/bin/env python3

"""
./manhattan-2.py plink.#.qassocc 
"""

import sys
import itertools
import os
import matplotlib.pyplot as plt
import numpy as np
import math

qassoc = open(sys.argv[1])
name = str(sys.argv[2])

header = qassoc.readline()
data = {}

for line in qassoc: 
    fields = line.split()
    if fields[-1] == 'NA':
        continue
    chrom = fields[0]
    pos = int(fields[2])
    p = float(fields[-1])
    logp = -np.log10(p)
    
    if chrom not in data:
        data[chrom] = {'positions':[], 'logpvals':[]}
    data[chrom]['positions'].append(pos)
    data[chrom]['logpvals'].append(logp)


# Building the manhattan plot

fig, ax = plt.subplots(figsize=(20,5))

colors = ['skyblue', 'sandybrown'] # colors for non sig values
highlights = ['steelblue', 'coral'] # colors for significant values

offset = 0 #use to shift each chromsome position over to next chromosome
tick_pos = []
tick_labels = []
for i,chrom in enumerate(data.keys()):
    x = np.array(data[chrom]['positions']) #need to make them an array to do sig
    y = np.array(data[chrom]['logpvals'])

    sig = (y > 5)

    ax.scatter(x[sig] + offset, y[sig], marker = '.', color = highlights[i%2]) #alternates between colors '%'
    ax.scatter(x[~sig] + offset, y[~sig], marker = '.', color = colors[i%2])

    tick_labels.append(chrom)

    maxx = max(x)
    tick_pos.append(offset + maxx/2)
    offset += maxx 

ax.set_xticks(tick_pos)
ax.set_xticklabels(tick_labels);

ax.axhline(5, color = 'k', ls = ':', label = "Significance Cutoff")
ax.legend()
ax.set_xlabel("Genomic position")
ax.set_ylabel("Log10 P-value")
ax.set_title(name)
plt.savefig('graphs/' + name + '.png')
plt.close()
