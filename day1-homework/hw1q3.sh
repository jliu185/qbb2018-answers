#!/bin/bash

grep -v "^@" ~/qbb2018-answers/day1-afternoon/SRR072893/SRR072893.sam | grep -v ^211 | cut -f 3 | sort | uniq -c

