#!/usr/bin/env python3

# Finding fpkm, and calcualte mean and stdev

import sys


fly_dict = {}
for line in open(sys.argv[1]):
    if "_DROME" not in line:
        continue
    fields = line.strip("\r\n").split()
    if fields[-1].startswith("FBgn"):
       fly_dict.update({fields [3] : fields [2]})
       #print (fly_dict)

c_tab = []
for i, line in enumerate(open(sys.argv[2])): #enumerate allows us to loop over something and have an automatic counte. 
    if i == 0:
        continue
    fields = line.rstrip("\r\n").split("\t")
# THIS IS STANDARD FOR ALL TABULAR SORTING/FINDING
    fbgn = fields[8]
    if fbgn in fly_dict.keys():
        unip = fly_dict[fbgn]
        print (line.rstrip('\r\n') + "\t" + unip)
    else: 
        print (line.rstrip('\r\n') + "\t" + "no match")
        
    
        