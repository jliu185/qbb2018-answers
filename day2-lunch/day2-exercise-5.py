#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open ( sys.argv[1] )
else: 
    f = sys.stdin
#calling the sam file
 
mapq = [] 
for i, line in enumerate( f ):
    if i == 0:
        continue #skip header
    if line.startswith ("@"):
        continue
    fields = line.strip("\r\n").split("\t") 
    mapq.append(int(fields[4]))


avg = sum(mapq)/len(mapq)
print (avg)
    
        
    
    