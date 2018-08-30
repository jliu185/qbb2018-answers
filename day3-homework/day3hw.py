#!/usr/bin/env python3

import sys
import fasta

print('tar_sequence_name', 'query start', 'target start', 'kmer')

target_fa = open(sys.argv[1]) # target sequence file
query_fa = open(sys.argv[2]) # query sequence file
k = int(sys.argv[3]) # k length for the kmers

# Lets make a dictioanry of the target sequence
t_dic = {}    
for ident, sequence in fasta.FASTAReader(target_fa): 
    for i in range(0,len(sequence) - k): #establishes range of grabbing kmers, with -k preventing hangovers from being grabbed
        kmer_t = sequence[i:i+k] #creates kmer
        if kmer_t not in t_dic:
            t_dic[kmer_t] = [[ident, i]] #adds each kmer to dictionary at position i, and also adds name of fasta as one of the values. We make a list here to organize the kmers appropriately
        else:
            t_dic[kmer_t].append([ident, i]) #adds repeat kmer to same list

# ident = identity/name of Fasta
# sequence = sequence associated with that FASTA

for ident1, sequence1 in fasta.FASTAReader(query_fa): # faster reader for query sequence (note the change in index and variables!)
    for j in range(0,len(sequence1) - k):
        kmer_q = sequence1[j:j+k] #create only kmers for query sequence
        if kmer_q in t_dic.keys(): #.keys returns all keys in the dictioanry, and this code identifies kmers in query that match the kmers in our target dictionary by POSITION
            result = t_dic[kmer_q]
            for hit in result: #hit unravels the lists of lists
                print(hit[0], i, j, hit[1])
             
    
