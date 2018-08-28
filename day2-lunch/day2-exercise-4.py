#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    f = open ( sys.argv[1] )
else: 
    f = sys.stdin
#calling the sam file
 
c_list = [] 
for i, line in enumerate( f ):
    if i == 0:
        continue #skip header
    if line.startswith ("@"):
        continue
    fields = line.strip("\r\n").split("\t") 
    c_list.append(fields[2])
    if len(c_list) > 10:
        print (c_list)
        break

