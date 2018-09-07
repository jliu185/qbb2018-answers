#!/usr/bin/env python

"""
Reads a peptide sequence and puts the nucleotide sequence from a .fasta file. Puts three -'s for every blank in the peptide
./pep_nuc_parser.py <query_1000.fa> <peptide_alignment.fa>
"""

import sys
import fasta
import itertools


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

print(all_nuc)
print(all_aa)












# for ident, sequences in fasta.FASTAReader(pep):
#     pep_seq.append(sequences)
#     fasta_ident.append(ident)
#
# for ident, sequences in fasta.FASTAReader(nuc):
#     nuc_seq.append(sequences)
#     print (nuc_seq)

