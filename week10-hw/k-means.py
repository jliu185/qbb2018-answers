#!/usr/bin/env python3

"""
Usage: ./k-means.py hema_data.txt
"""

import numpy as np
import pandas as pd
import sys
from scipy.cluster.hierarchy import dendrogram, linkage, leaves_list
from scipy.spatial.distance import pdist
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

file = open(sys.argv[1])

d = pd.read_csv(file, sep="\t", index_col='gene')
df = pd.DataFrame(d)

#Making K-means
kmeans = KMeans(n_clusters=5,random_state=0)
kmeans.fit(df)
y_kmeans = kmeans.predict(df)

#plot
fig = plt.figure(figsize=(25, 10))
plt.title('k-means Plot')
plt.scatter(df["CFU"], df['poly'], c=y_kmeans, s=200, cmap='gist_rainbow')
plt.ylabel("poly expression")
plt.xlabel("CFU expression")
plt.savefig("kmeans-plot.png")
plt.close()


















