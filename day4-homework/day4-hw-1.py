#!/usr/bin/env python3

"""
Usage: ./02-boxplot.py <samples.csv> <samples tsv> <ctab.dir>

Create a boxplot for a given name in each sample
tsv = tab separated file
"""

import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv(sys.argv[1]) #gathering the csv file

all_d = {}

for index, sample, sex, stage in df.itertuples(): 
    filename = os.path.join(sys.argv[2], sample, "t_data.ctab") 
    ctab_df = pd.read_table (filename, index_col = "t_name").loc[:,"FPKM"]
    all_d[str(sex) + str(stage)]=ctab_df
df = pd.DataFrame(all_d)
df.to_csv(sys.stdout)

