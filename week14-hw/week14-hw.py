#!/usr/bin/env python3

"""
Usage: 
"""

import sys

import matplotlib
matplotlib.use("Agg")
import scanpy.api as sc
sc.settings.autoshow = False

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")

# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

# #Producing a PCA plot before filtering
sc.tl.pca(adata)
sc.pl.pca(adata, save = "unfiltered_pca.png")
# Filter data and produce and plot a PCA plot
filt = sc.pp.recipe_zheng17(adata, n_top_genes=1000, log=True, plot=False, copy=True)
sc.pl.pca(filt, save="filtered_pca.png")

# Clustering using t-test and logistic regression
sc.pp.neighbors(filt, n_neighbors=15, n_pcs=50, use_rep=None, knn=True, random_state=0, metric_kwds={})
sc.tl.louvain(filt)
sc.tl.tsne(filt, n_pcs = 50)
sc.pl.tsne(filt, save="tsne.png")
sc.tl.umap(filt)
sc.pl.umap(filt, save="UMAP.png")

# Distinguishing genes via t-test
sc.tl.rank_genes_groups(filt, groupby = 'louvain', method = 't-test')
sc.pl.rank_genes_groups(filt, save = "ttest.png")
# Distinguishing genes via logistic regression
sc.tl.rank_genes_groups(filt, groupby = 'louvain', method = 'logreg')
sc.pl.rank_genes_groups(filt, save = "logreg.png")

# Looking at Cell types with TSNE plots
sc.pl.tsne(filt, color = ["louvain", "Tubb2b"], save="cluster0_Tubb2b.png")
sc.pl.tsne(filt, color = ["louvain", "Tmsb10"], save="cluster1_Tmsb10.png")
sc.pl.tsne(filt, color = ["louvain", "Tmsb4x"], save="cluster2_Tmsb4x.png")
sc.pl.tsne(filt, color = ["louvain", "Rps4x"], save="cluster3_Rps4x.png")
sc.pl.tsne(filt, color = ["louvain", "mt-Atp6"], save="cluster4_mt-Atp6.png")
sc.pl.tsne(filt, color = ["louvain", "mt-Co2"], save="cluster5_mt-Co2.png")
sc.pl.tsne(filt, color = ["louvain", "Stmn1"], save="cluster6_Stmn1.png")
sc.pl.tsne(filt, color = ["louvain", "mt-Co3"], save="cluster7_mt-Co3.png")
sc.pl.tsne(filt, color = ["louvain", "Malat1"], save="cluster8_Malat1.png")
sc.pl.tsne(filt, color = ["louvain", "mt-Co1"], save="cluster9_mt-Co1.png")
sc.pl.tsne(filt, color = ["louvain", "Eef1a1"], save="cluster10_Eef1a1.png")

