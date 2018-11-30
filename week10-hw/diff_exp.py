#!/usr/bin/env python3

"""
Usage: ./diff_exp.py hema_data.txt
"""

import numpy as np
import pandas as pd
import sys
from scipy import stats
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

file = open(sys.argv[1])

list_of_genes = []
upreg_gene = "none"

for line in enumerate(file):
    for i, line in enumerate(file):
        if i ==0:
            continue
        fields = line.rstrip("\r\n").split("\t")
        gene_name = fields[0]
        cfu = float(fields[1])
        poly = float(fields[2])
        unk = float(fields[3])
        mys = float(fields[5])
        early_avg = (cfu+mys)/2
        late_avg = (poly+unk)/2
        fold_chng = early_avg/late_avg
        t_stat, p_val = stats.ttest_ind([cfu, mys], [poly, unk])
        if fold_chng >= 2 or fold_chng <= 0.5 and p_val < 0.5:
            list_of_genes.append([gene_name, p_val])
            if fold_chng > 0:
                fold_chng = 0
                upreg_gene = gene_name
                
text_file = open('diff_exp_genes.txt','w')
for i, word in enumerate(list_of_genes):
    if i == 0:
        text_file.write("gene name")
        text_file.write("\t")
        text_file.write("p-value")
        text_file.write("\n")
    text_file.write(str(list_of_genes[i][0]))
    text_file.write("\t")
    text_file.write(str(list_of_genes[i][1]))
    text_file.write("\n")
text_file.close()
            