#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open ( sys.argv[1] )
else: 
    f = sys.stdin
#calling the sam file

count = 0    
for i in f:  
    if i == 0:
        continue #skip header
    elif "NM:i:0" in i:
        count += 1

print(count)    