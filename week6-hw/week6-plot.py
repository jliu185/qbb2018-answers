#!/usr/bin/env python3

"""
./week6-plot.py diff_gained_peaks.bed diff_lost_peaks.bed Mus_musculus.GRCm38.94_features.bed

"""

import sys
import matplotlib.pyplot as plt
import numpy as np

x1 = open(sys.argv[1])
x2 = open(sys.argv[2])
x3 = open(sys.argv[3])

# make dictionary with key as bp and value as exon/intron/promoter
feat_dict = {}
for line in x3:
    fields = line.rstrip("\r\n").split("\t")
    start = int(fields[1])
    end = int(fields[2])
    feat = fields[3]
    for bp in range(start,end):
        feat_dict[bp] = feat

# plot number of CTCF sites lost and gained in G1E --> ER4 cells + reference dict to that site
gain_peak = 0
masterlist_gained = []
for i, line in enumerate(x1):
    feat_gained = []
    gain_peak += 1
    fields = line.rstrip("\r\n").split("\t")
    gain_start = int(fields[1])
    gain_end = int(fields[2])
    for bp in range(gain_start, gain_end):
        if bp in feat_dict:
            gain_feat = feat_dict[bp] 
            if gain_feat not in feat_gained:
                feat_gained.append(gain_feat)
    masterlist_gained.append(feat_gained)   


exon_gained = 0
intron_gained = 0
promoter_gained = 0
for i in masterlist_gained:
    if len(i) == 0:
        continue
    for sublist in i:
        if sublist == "exon":
            exon_gained += 1
        if sublist == "intron":
            intron_gained += 1
        if sublist == "promoter":
            promoter_gained += 1

#CTCF sites lost with reference to feature dictionary
lost_peak = 0
masterlist_lost = []
for i, line in enumerate(x2):
    feat_lost = []
    lost_peak += 1
    fields = line.rstrip("\r\n").split("\t")
    lost_start = int(fields[1])
    lost_end = int(fields[2])
    for bp in range(lost_start, lost_end):
        if bp in feat_dict:
            lost_feat = feat_dict[bp] 
            if lost_feat not in feat_lost:
                feat_lost.append(lost_feat)
    masterlist_lost.append(feat_lost)

exon_lost = 0
intron_lost = 0
promoter_lost = 0
for i in masterlist_lost:
    if len(i) == 0:
        continue
    for sublist in i:
        if sublist == "exon":
            exon_lost += 1
        if sublist == "intron":
            intron_lost += 1
        if sublist == "promoter":
            promoter_lost += 1

#Creating graphs
ticks = [0, 0.25]
ticks2 = [0, 1, 2]
tick_labels = ["gained", "lost"]
tick_labels2 = ["exons", "introns", "promoter"]
fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(20,5))
ax1.bar(0, exon_gained, color="orange", label="CTCF sites gained in ER4 cells")
ax1.bar(1, intron_gained, color="orange")
ax1.bar(2, promoter_gained, color="orange")
ax1.bar(0, exon_lost, color="cyan", label="CTCF sites lost in ER4 cells")
ax1.bar(1, intron_lost, color="cyan")
ax1.bar(2, promoter_lost, color="cyan")
ax1.set_xticks(ticks2)
ax1.set_xticklabels(tick_labels2)
ax1.set_ylabel("Number of CTCF binding sites")
ax1.set_title("Number of CTCF binding sites for each type of region in ER4 or G1E cells")
ax1.legend()

ax2.bar(0, gain_peak, width=0.1, color="orange", align="center", label="CTCF sites gained in ER4 cells")
ax2.bar(0.25, lost_peak, width=0.1, color="cyan", align="center", label="CTCF sites lost in ER4 cells")
ax2.set_xticks(ticks)
ax2.set_xticklabels(tick_labels)
ax2.set_ylabel("Number of CTCF binding sites")
ax2.set_title("Number of CTCF binding sites gained/lost from G1E --> ER4 cells")
ax2.legend()

fig.savefig("chip_seq_plot.png")
plt.close(fig)