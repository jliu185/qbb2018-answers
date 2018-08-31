#!/usr/bin/env python3

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name")
fpkm1 = df1.loc[:,"FPKM"]
df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name")
fpkm2 = df2.loc[:,"FPKM"]

M_plot = np.log2((fpkm1+1)/(fpkm2+1)) 
A_plot = 0.5 * (   np.log2(fpkm1+1) + np.log2(fpkm2+1)   ) 

fig, (ax) = plt.subplots()
ax.scatter(A_plot, M_plot, alpha = 0.1, s=2, color="blue")
ax.set_title("Comparative gene expression between SRR072893 and SRR072915")
ax.set_xlabel("avg. intensity (A) [log2(FPKM1/FPKM2)]")
ax.set_ylabel("intensity ratio (M) 1/2(log2(FPKM1) + log2(FPKM2))")
fig.savefig("ma_plot.png")
plt.close()





