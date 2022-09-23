#!/bin/bash
#PBS -l nodes=1:ppn=32 
#PBS -l walltime=04:00:00
#PBS -l gres=ccm
#PBS -N allign_SRR3228431

module load ccm
module load hisat/0.1.6
module load samtools/1.2

cd /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams

ccmrun hisat -p 32 -q -x /N/dc2/projects/MAMMALEXP/RBP-Target-Evolution_and_Transcriptome_Dynamics/REFERENCE/Human/h38.84/h38.84 -1 /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/fastqs_GSE79249/SRR3228431_1.fastq -2 /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/fastqs_GSE79249/SRR3228431_2.fastq -S /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/SRR3228431.sam
ccmrun samtools view -S -b /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/SRR3228431.sam > /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/SRR3228431.bam
ccmrun samtools sort /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/SRR3228431.bam /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/SRR3228431.sorted
ccmrun samtools index /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/SRR3228431.sorted.bam


