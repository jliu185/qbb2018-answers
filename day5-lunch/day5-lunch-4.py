#!/usr/bin/env python3

"""
./day5.lunch-4.py <.tab> <.ctab>
"""

import sys
import numpy as np
import statsmodels.formula.api as sm
import matplotlib.pyplot as plt
import pandas as pd

#pulling out the avg regions from the bigWigAverageOverBed 
df1 = pd.read_csv(sys.argv[2], sep="\t", index_col=0).iloc[:,4]
df2 = pd.read_csv(sys.argv[3], sep="\t", index_col=0).iloc[:,4]
df3 = pd.read_csv(sys.argv[4], sep="\t", index_col=0).iloc[:,4]
df4 = pd.read_csv(sys.argv[5], sep="\t", index_col=0).iloc[:,4]
df5 = pd.read_csv(sys.argv[6], sep="\t", index_col=0).iloc[:,4]

# pulling out the FPKMS from the ctab file
df_ctab = pd.read_csv(sys.argv[1], sep="\t", index_col = "t_name")
coi = ["FPKM"]
fpkm_ctab= df_ctab.loc[:,coi]

#combining the FPKMS and bigWigAverageOverBed avg files and making headers for each file
df_sort = pd.concat([df1, df2, df3, df4, df5, fpkm_ctab], ignore_index = True, axis=1, sort=True)
df_sort.rename(index = str, columns={ 0:"H3K27ac", 1:"H3K27me3", 2:"H3K4me1", 3:"H3K4me3",4:"H3K9ac",5:"FPKMs"}, inplace = True)

# ordinary linear regression equation using statsmodels
fxn_olr = 'FPKMs ~ H3K27ac + H3K27me3 + H3K4me1 + H3K4me3 + H3K9ac'
results=sm.ols(formula=fxn_olr, data=df_sort).fit()
print(results.summary())



