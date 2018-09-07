#!/usr/bin/env python3

"""
Parse ALL FASTA records from stdin and print id and sequence

"""

import sys

class FASTAReader(object): #

    def __init__(self, file):
        self.last_ident = None
        self.file = file
        self.eof = False #indicates end of the file

    def __iter__(self):
        return self

    def __next__(self):
        
        if self.eof:
            #return None, None
            raise StopIteration
        
        if self.last_ident is not None:
            #Not first line
            ident = self.last_ident
        
        else:
            # First Line
            line = self.file.readline() #want to selectively read files, specifically the header
            assert line.startswith(">"), "Not a FASTA file" #recognizes the headers in the FASTA file
            ident = line[1:].rstrip("\r\n") # recognizes first character and strips file 

        sequences = []
        while True:
            line = self.file.readline()
            if line == "":
                self.eof = True
                break
            elif not line.startswith(">"):
                sequences.append(line.strip())
            else:
                self.last_ident = line[1:].rstrip("\r\n")
                break

        sequence = "".join(sequences) #""=delimitor that could be tab, etc. 
        return ident, sequence

##WHAT WE WANT!

#reader = FASTAReader(sys.stdin)

#for ident, sequence in reader:
#    print (ident, sequence)

#while True:
#    ident, sequence = reader.next()
#    if ident is None:
#        break
#    print(ident,sequence)
    
    
    