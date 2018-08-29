#!/usr/bin/env python3

import sys

count = 0
gene_dict = {}
for i, line in enumerate(sys.stdin):  
    if line[0] == "#":
          continue
    fields = line.rstrip("\r\n").split()

  # THIS IS STANDARD FOR ALL TABULAR SORTING/FINDING
    gene_column = fields[2]
    # print (gene_column)
    

    for j, field in enumerate(fields):
        if field == "gene_biotype":
           prot_column = fields[j + 1] 
           if prot_column not in gene_dict:
               gene_dict[prot_column]=1
           else:
               gene_dict[prot_column]+=1

print (gene_dict)
           