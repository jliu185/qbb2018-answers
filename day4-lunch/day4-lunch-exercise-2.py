#!/usr/bin/env python3

"""
"""

import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv(sys.argv[1], sep="\t", index_col="t_name").loc[:,"FPKM"]
log_df1 = np.log(df1 + 1)

df2 = pd.read_csv(sys.argv[2], sep="\t", index_col="t_name").loc[:,"FPKM"]
log_df2 = np.log(df2 + 1)

# Scatter plot
fig, ax = plt.subplots()
ax.set_title("SRR072893 vs SRR072915")
ax.scatter(df1, df2)
ax.set_xlabel("SRR072893")
ax.set_ylabel("SRR072915")
fig.savefig("scatter.png")
plt.close(fig)

#Log scatter plot
fig, ax = plt.subplots()
ax.set_title("log SRR072893 vs SRR072915")
ax.scatter(log_df1, log_df2)
ax.set_xlabel("log SRR072893")
ax.set_ylabel("log SRR072915")
fig.savefig("log_scatter.png")
plt.close(fig)

#Log scatter plot with adjusted transparency
fig, ax = plt.subplots()
ax.set_title("log SRR072893 vs SRR072915")
ax.scatter(log_df1, log_df2, alpha = 0.03)
ax.set_xlabel("log SRR072893")
ax.set_ylabel("log SRR072915")
fig.savefig("log_trans_scatter.png")
plt.close(fig)

#Polyfit
fit = np.polyfit(log_df1, log_df2, 1) # returns coefficients of model ax+b
poly_x_value = np.linspace(0,10)
poly_y_value = np.poly1d(fit)

fig, ax = plt.subplots() #REQUIRED
ax.scatter(log_df1, log_df2, alpha = 0.03)
ax.set_xlabel("log SRR072893")
ax.set_ylabel("log SRR072915")
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)
plt.plot(poly_x_value, poly_y_value(poly_x_value), 'k')
plt.text(7,5,str(poly_y_value))
fig.savefig("polyfit_scatter.png") 
plt.close(fig) 

