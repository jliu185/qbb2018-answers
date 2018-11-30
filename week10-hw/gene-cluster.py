#!/usr/bin/env python3

"""
Usage: ./gene-cluster.py hema_data.txt
"""

import numpy as np
import pandas as pd
import sys
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy.spatial.distance import pdist
import matplotlib.pyplot as plt
import seaborn as sns

file = open(sys.argv[1])

data = pd.read_csv(file, sep="\t", index_col='gene')
df = pd.DataFrame(data)

ax = sns.clustermap(df, metric="euclidean", standard_scale=1, method="ward", cmap="Blues")
ax.savefig("dendrogram_heat_map_combined.png")
plt.close()





    
