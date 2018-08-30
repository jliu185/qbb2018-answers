#!/usr/bin/env python3

"""
Usage: ./day4lunch.py <threshold> <ctab_file i> <ctab_file j> 

Create csv file with FPKMs from 2 samples
- assumes ctab file in directory with the same name
"""

import sys
import os
import pandas as pd

#
thres = int(sys.argv[1]) 

#grabbing "n" number of ctabs and creating the list of ctabs
num_ctab = len(sys.argv) - 2
list_ctab = sys.argv[2:len(sys.argv)]

dic={}
for file in list_ctab:
    name = file.split(os.sep)[-2] 
    fpkm = pd.read_csv(file, sep="\t", index_col="t_name").loc[:,"FPKM"]
    dic[name] = fpkm

fpkm_all = pd.DataFrame(dic)
sum_col = fpkm_all.sum(axis=1)
fpkm_tot = fpkm_all.assign(sum = sum_col)
print(fpkm_tot)
fpkm_filt = fpkm_tot.loc[:,"sum"] > float(thres)
print(fpkm_tot.loc[fpkm_filt,:])

   
   
