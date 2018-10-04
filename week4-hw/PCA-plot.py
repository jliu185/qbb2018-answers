#!/usr/bin/env python

"""
Usage:
./pca_grapher.py <plink.eigenvec>
"""

import sys
import matplotlib.pyplot as plt

xval,yval = [],[]
for line in open(sys.argv[1]):
    PCs = line.rstrip('\r\n').split(' ')
    xval.append(float(PCs[2]))
    yval.append(float(PCs[3]))

plt.figure()
plt.scatter(xval,yval)
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Principle Component Analysis')
plt.savefig('PCA_plot')
plt.close()