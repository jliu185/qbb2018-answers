#!/usr/bin/env python3

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
log_fpkm_ctab = np.log(fpkm_ctab+1)

#combining the FPKMS and bigWigAverageOverBed avg files and making headers for each file
df_sort = pd.concat([df1, df2, df3, df4, df5, log_fpkm_ctab], ignore_index = True, axis=1, sort=True)
df_sort.rename(index = str, columns={ 0:"H3K27ac", 1:"H3K27me3", 2:"H3K4me1", 3:"H3K4me3",4:"H3K9ac",5:"log_FPKMs"}, inplace = True)

# ordinary linear regression equation using statsmodels
fxn_olr = 'log_FPKMs ~ H3K27ac + H3K27me3 + H3K4me1 + H3K4me3 + H3K9ac'
results=sm.ols(formula=fxn_olr, data=df_sort).fit()
print(results.summary())
# print residuals
print(results.resid)

# plotting residual plot
fig, ax = plt.subplots()
ax.hist(results.resid, bins =500)
ax.set_xlim(-10,10)
fig.savefig("day5_exercise_6.png")
plt.close(fig)