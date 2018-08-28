#!/usr/bin/env python3

# Finding fpkm, and calcualte mean and stdev

import sys

c_tab = []

for i, line in enumerate(sys.stdin): #enumerate allows us to loop over something and have an automatic counte. 
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
# THIS IS STANDARD FOR ALL TABULAR SORTING/FINDING
    fbgn = fields[9]
    c_tab.append(fbgn) #adds all IDs to empty list, and makes them into actual numbers
    print(fbgn)
 
