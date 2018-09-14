#!/usr/bin/env python

"""
./DN_dS.py <query_1000.fa> <peptide_alignment.fa>
"""

import sys
import fasta
import itertools
import matplotlib.pyplot as plt
import numpy as np
import math

nuc_reader = fasta.FASTAReader(open(sys.argv[1]))
pep_reader = fasta.FASTAReader(open(sys.argv[2]))

all_nuc = [] 
all_aa = []

for (dna_id,dna),(aa_id,aa) in zip(nuc_reader,pep_reader):
    nuc_seq = []
    aa_list = []    
    j = 0
    for i in range(len(aa)):
        a=aa[i]
        aa_list.append(a)
        nuc = dna[j*3:(j+1)*3]
        if a == "-":
            nuc_seq.append("---")
        else:
            nuc_seq.append(nuc)
            j += 1
    all_nuc.append(nuc_seq)
    all_aa.append(aa_list)

# Calculate the dn and ds at each position in the alignment

query_aa = all_aa[0]
query_nuc = all_nuc[0]
dS_list = [0] * len(query_aa)
dN_list = [0] * len(query_aa)
    
# Iterate through each alignment in the list
for nuc_list, aas_list in zip(all_nuc[1:], all_aa[1:]):
    for i in range(0, len(nuc_list)):
        if query_nuc[i] == "---":
            continue
        elif nuc_list[i] != query_nuc[i]:
            if aas_list[i] == query_aa[i]:
                dS_list[i] += 1
            else:
                dN_list[i] += 1

# adds one to every sequence in dN and dS to take away non-zero values for log graph into 
# their respective lists
nonz_dN = []
nonz_dS = []

for i in range(len(dS_list)):
    nonz_dN.append(dN_list[i] + 1)
    nonz_dS.append(dS_list[i] + 1)

#makes a log(dNdS) list for separating out positively selected groups
log_nonz_dNdS = [np.log2(float(n)/float(s)) for n,s in zip(nonz_dN, nonz_dS)]

#making a list of positive selected values, and regular values
pos_sel = []
log_dNdS = []

#Keeps index in range
for i in range(len(log_nonz_dNdS)):
    pos_sel.append(None)
    log_dNdS.append(None)

for i in range(len(log_nonz_dNdS)):
    if log_nonz_dNdS[i] > 9.50:
        pos_sel[i] = log_nonz_dNdS[i]
    else:
        log_dNdS[i] = log_nonz_dNdS[i]

# makes new list that subtracts every non zero dN from dS at every 
# single index in the list
log_nonz_dNdS = [(float(n)/float(s)) for n,s in zip(nonz_dN, nonz_dS)]

# calculates mean, standard deviation, and z-score for log adjusted dN-dS
mean_nonz_dNdS = np.mean(log_nonz_dNdS)
stdv_nonz_dNdS = np.std(log_nonz_dNdS)
stderr_nonz_dNdS = stdv_nonz_dNdS / np.sqrt(len(log_nonz_dNdS))
zscore_nonz_dNdS = (mean_nonz_dNdS-0) / stderr_nonz_dNdS

# Plot of dN and dS, and positively selected values
fig, ax = plt.subplots()
ax.scatter(range(len(log_dNdS)), log_dNdS, alpha=.5, color ="blue")
ax.scatter(range(len(pos_sel)), pos_sel, alpha=.5, color = "red")
plt.title('dN-dS scatter plot', fontsize='20')
plt.xlabel("Gene Positions in the Sequence")
plt.ylabel("log2(dN/dS)")
plt.figtext(0.28, 0.96, "non zero zscore = " + str(zscore_nonz_dNdS))
plt.savefig( "dNdS_zscore.png")
plt.close(fig)
