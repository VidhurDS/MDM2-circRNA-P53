#!/bin/bash
#PBS -l nodes=1:ppn=32 
#PBS -l walltime=10:00:00
#PBS -l gres=ccm
#PBS -N download_SRR3228432

module load ccm

cd /N/dc2/projects/CancerFight/Vidhur/fastqs_GSE79249

ccmrun /gpfs/home/s/w/swapdaul/BigRed2/sratoolkit.2.8.2-1-ubuntu64/bin/fastq-dump --split-files --gzip SRR3228432


