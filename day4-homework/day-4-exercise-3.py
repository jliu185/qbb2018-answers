#!/usr/bin/env python3

"""
Usage: ./03-boxplot.py <samples tsv> <ctab.dir> <replicates.csv>

Create a timecourse of a given transcript (FBtr0331261) for females

"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv(sys.argv[1])
print(df1)
ctab_file = sys.argv[2]
gene_name = sys.argv[3]


for gene in sys.argv[3:]:
    def timecourse(gender, df, gene_name):
        soi = df.loc[:,"sex"] == gender
        df = df.loc[soi,:]
        fpkms = []
        stages = []

        for index, sample, sex, stage in df.itertuples(): 
            filename = os.path.join(ctab_file, sample, "t_data.ctab") 
            ctab_df = pd.read_table (filename) 
            roi = ctab_df.loc[:,"gene_name"] == gene_name
            fpkms.append(ctab_df.loc[roi,"FPKM"].mean())
            stages.append(stage)
        return fpkms, stages

#for gene in gene_name.split(','):
female, stages = timecourse('female', df1, gene)
male, stages = timecourse('male', df1, gene)
    
fig, ax = plt.subplots()
ax.plot(female, color='red', label = 'female')
ax.plot(male, color='blue',label = 'male')
plt.xlabel('developmantal stage')
plt.ylabel('mean mRNA abundance (RPKM)')
plt.title(gene, style='italic', fontsize='20')
plt.xticks(np.arange(8), ('10', '11', '12', '13', '14A', '14B', '14C', '14D'), rotation=90)
plt.legend(bbox_to_anchor=(1.03,0.55), loc=2,borderaxespad = 0.)
fig.savefig(gene,bbox_inches = 'tight')
plt.close(fig)
    
    


