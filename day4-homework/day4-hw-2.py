#!/usr/bin/env python3

"""
Usage: ./03-boxplot.py <samples tsv> <ctab.dir>

Create a timecourse of a given transcript (FBtr0331261) for females

"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(sys.argv[1])
transcript = 'FBtr0331261'

def timecourse(gender, df):
    fpkms = []
    soi = df.loc[:,"sex"] == gender
    df = df.loc[soi,:]
    for index, sample, sex, stage in df.itertuples(): 
        filename = os.path.join(sys.argv[2], sample, "t_data.ctab") 
        ctab_df = pd.read_table (filename, index_col = "t_name") 
        roi = ctab_df.loc[:,"gene_name"] == transcript
        fpkms.append(ctab_df.loc[transcript,"FPKM"])
    return fpkms

fpkm_f = timecourse('female', df)
fpkm_m = timecourse('male', df)

# plotting 
fig, ax = plt.subplots()
ax.plot(fpkm_f, color='red', label = 'female')
ax.plot(fpkm_m, color='blue',label = 'male')


plt.xlabel('developmantal stage')
plt.ylabel('mRNA abundance (RPKM)')
plt.title('Sxl', style='italic', fontsize='20')
plt.xticks(np.arange(8), ('10', '11', '12', '13', '14A', '14B', '14C', '14D'), rotation=90)
plt.legend(bbox_to_anchor=(1.03,0.55), loc=2,borderaxespad = 0.)
fig.savefig("timecourse.png",bbox_inches = 'tight')
plt.close(fig)   
    