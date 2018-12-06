#!/usr/bin/env python

"""
Usage: ctcf.py GSM2418860_WT_CTCF_peaks.txt
"""

import sys
import hifive
import numpy

file = open(sys.argv[1])

list_mp = []

# Making midpoints from original txt file
for i, line in enumerate(file):
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
    chromo = fields[0]
    start = int(fields[1])
    end = int(fields[2])
    if chromo == "chr17" and start >=15000000 and end <=17500000:
        midpoint = (end-start)/2
        mp_chr = (start + midpoint)
        list_mp.append(mp_chr)

# Making 3-D array from hcp file
hic = hifive.HiC('week13.hcp')
data = hic.cis_heatmap(chrom='chr17', start=15000000, stop=17500000, binsize=10000, datatype='fend', arraytype='full')

data[:, :, 1] *=numpy.sum(data[:, :, 0]) / numpy.sum(data[:, :, 1])
where = numpy.where(data[:, :, 1] > 0)
data[where[0], where[1], 0] /= data[where[0], where[1], 1]
data = data[:, :, 0]

# Creating bin numbers from txt file and 
bin_list = []
bin_size = 10000
chr17_start= 15000000
for value in list_mp:
    new_value = (value - chr17_start)/bin_size
    bin_list.append(new_value)

# Finding values from midpoint in data array
new_ctcf_list = numpy.unique(bin_list)
enriched_values = []

for i in range(len(new_ctcf_list)):
    for j in range(i,len(new_ctcf_list)):
        if data[new_ctcf_list[i],new_ctcf_list[j]] > 1:
            enriched_values.append((new_ctcf_list[i],new_ctcf_list[j],data[new_ctcf_list[i],new_ctcf_list[j]]))

# Converting back to genomic position
new_gen_pos_list=[]

for bin_row, bin_col, enrichment in enriched_values:
    gen_row = (10000*bin_row) + 15000000
    gen_col = (10000*bin_row) + 15000000 
    new_gen_pos_list.append((gen_row,gen_col,enrichment))

# Printing out genomic values 
sorted_new_gen_pos_list = sorted(new_gen_pos_list, key = lambda t:t[2], reverse=False)

for row, column, value in sorted_new_gen_pos_list:
    print(str(row) + "\t" + str(column) + "\t" + str(value))





        