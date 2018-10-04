#!/usr/bin/env python

"""
Usage:
./all-freq.py <vcf>
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("ggplot")

vcf = open(sys.argv[1])

all_freq = []

for line in vcf:
    if line.startswith('#'):
        continue
    else:
        segs = line.rstrip('\r\n').split('\t')
        all_freqs = segs[7].lstrip('AF=').split(',')
        for freq in all_freqs:
            all_freq.append(float(freq))

plt.figure()
plt.hist(all_freq, bins=1000)
plt.xlabel('allele frequency')
plt.ylabel('counts')
plt.title( 'Allele frequencies from ~1000 strains in yeast genome' )
plt.savefig('all_freq.png')
plt.close()