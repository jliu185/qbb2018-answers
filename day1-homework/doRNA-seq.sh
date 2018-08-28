#!/bin/bash

GENOME=~/qbb2018-answers/Genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  mkdir $SAMPLE
  fastqc ~/data/rawdata/${SAMPLE}.fastq
  hisat2 -x ${GENOME} -U ~/data/rawdata/${SAMPLE}.fastq -p 4 -S ~/data/rawdata/${SAMPLE}.sam
  samtools view -b ~/data/rawdata/${SAMPLE}.sam -o ~/data/rawdata/${SAMPLE}.bam           
  samtools sort ~/data/rawdata/${SAMPLE}.bam -o ~/data/rawdata/${SAMPLE}.bam.sort          
  samtools index ~/data/rawdata/${SAMPLE}.bam.sort
  stringtie -p 4 -e -B ~/data/rawdata/${SAMPLE}.bam.sort -G ${ANNOTATION} -o ~/data/rawdata/${SAMPLE}.gtf
done
