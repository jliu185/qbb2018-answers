#!/usr/bin/env python3

import sys

print("Flybase ID","Uniprot ID AC")

for i, line in enumerate(sys.stdin): #enumerate allows us to loop over something and have an automatic counte. 
    if "_DROME" not in line:
        continue
    fields = line.strip("\r\n").split()
    if len(fields) <4:
        continue
    # strip removes \r=return characters, \n new line characters
    # .split will split by tabs \t
# THIS IS STANDARD FOR ALL TABULAR SORTING/FINDING
    print(fields[3],fields[2])
    

    