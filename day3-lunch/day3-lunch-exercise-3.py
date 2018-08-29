#!/usr/bin/env python3

import sys

x = 21378950
my_dist = 0
s_dist = 10**9

for i, line in enumerate(sys.stdin):  
    if line[0] == "#":
          continue
    fields = line.rstrip("\r\n").split()
    gene_col = fields[2]
    chr_col = fields [0]
    chr_s_col = int(fields [3])
    chr_e_col = int(fields [4])

    for j, field in enumerate(fields):
       if field == "gene_biotype":
           prot_column = fields[j + 1] 
           
    for k, field in enumerate(fields):
       if field == "gene_name":
           gene_name_column = fields[k+1] 
    
           
        
    for l, val in enumerate(fields):
        if chr_col == "3R" and gene_col == "gene" and prot_column == '"protein_coding";':
            if x < chr_s_col:
                my_dist = chr_s_col - x
            elif x > chr_e_col:
                my_dist = x - chr_e_col
            if s_dist > my_dist:
                s_dist = my_dist
                closest_gene = gene_name_column
                
                
print(closest_gene, s_dist)
                
                

                
            
            
            
    
