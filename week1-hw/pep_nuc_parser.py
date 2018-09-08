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

all_nuc = [] #creating a list of all the nucleotides from the for loop
all_aa = [] #creating a list of all the aa from the for loop

for (dna_id,dna),(aa_id,aa) in zip(nuc_reader,pep_reader):
    nuc_seq = [] #creating a list for the extracted nucleotides
    aa_list = []    
    j = 0
    for i in range(len(aa)): 
        a=aa[i] #creating a list of all amino acid sequences through each alignment
        aa_list.append(a) #appending that list to another list
        nuc = dna[j*3:(j+1)*3] #counting codons per each triad of nucleotides
        if a == "-": #blank amino acid
            nuc_seq.append("---") #fill with 3 empty nucleotides
        else:
            nuc_seq.append(nuc) #else append the list with the list of nucleotides 
            j += 1 #increase the counter each time
    all_nuc.append(nuc_seq) #appending all the nucleotide sequences with amino acid gaps 
    all_aa.append(aa_list) #appending all the aa in a list

print(all_nuc)
print(all_aa)
