#!/usr/bin/env python

"""
./com_contig.py <contig.fa>
"""

import sys
import fasta
import matplotlib.pyplot as plt
import numpy as np
import math
import itertools

fa_file = fasta.FASTAReader(open(sys.argv[1]))

nuc_seq = []
nuc_len = []

#getting the sequences from each 
for ident, sequences in fa_file:
    nuc_seq.append(sequences)
# counting the length of each sequence    
for i in range(len(nuc_seq)):
    nuc_len.append(len(nuc_seq[i]))
    nuc_len.sort()

#print min, max, mean of fasta file    
print("Max = " + str(max(nuc_len)))
print("Min = " + str(min(nuc_len)))
print("Mean = " + str(np.mean(nuc_len)))

contig_len = 0
cum_contig_len = sum(nuc_len)

for i in nuc_len:
    contig_len += i
    if contig_len > (cum_contig_len/2):
        print("N50  = " + str(i))
        break

    

