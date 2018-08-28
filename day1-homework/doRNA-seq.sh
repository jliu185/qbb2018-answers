#!/bin/bash

GENOME=~/qbb2018-answers/Genomes/BDGP6
ANNOTATION=../genomes/BDGP6.Ensembl.81.gtf

for SAMPLE in SRR072893 SRR072903 SRR072905 SRR072915
do
  mkdir $SAMPLE
  fastqc ~/data/rawdata/${SAMPLE}.fastq
  hisat2 -x ${GENOME} -U ${SAMPLE}/${SAMPLE.fastq -p 4 -S ${SAMPLE}/${SAMPLE}.sam
  samtools view -b ${SAMPLE}/${SAMPLE}.sam -o {SAMPLE}/${SAMPLE}.bam           
  samtools sort ${SAMPLE}/${SAMPLE}.bam -o ${SAMPLE}/${SAMPLE}.bam.sort          
  samtools index ${SAMPLE}/${SAMPLE}.bam.sort
  stringtie -p 4 -e -B ${SAMPLE}/${SAMPLE}.bam.sort -G ${ANNOTATION} -o {SAMPLE}/${SAMPLE}.gtf
done
