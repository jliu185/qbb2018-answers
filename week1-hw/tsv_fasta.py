#!/usr/bin/env python

"""
Converting .tsv to .FASTA
tsv_fasta <filename.tsv> > output.fa
"""


import sys

tsv = open(sys.argv[1])



for i in tsv:
    fields = i.rstrip("\t\n").split("\t")
    print (">" + fields[0] + "\n" + fields[1].replace("-",""))
    