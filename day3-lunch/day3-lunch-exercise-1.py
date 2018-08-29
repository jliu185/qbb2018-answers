#!/usr/bin/env python3

import sys

count = 0
for i, line in enumerate(sys.stdin):  
    if line[0] == "#":
          continue
    fields = line.rstrip("\r\n").split()

  # THIS IS STANDARD FOR ALL TABULAR SORTING/FINDING
    gene_column = fields[2]
    # print (gene_column)
    
    
    for j, field in enumerate(fields):
       if field == "gene_biotype":
           #j += 1 
           prot_column = fields[j + 1] 
           #print(prot_column)
           if gene_column == "gene" and prot_column == '"protein_coding";':
               count += 1
        
print(count)
        
        
     
