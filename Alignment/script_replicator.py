with open("E:/Academic SoIC/SCJ/Dr. Ashish Lal/Alternative splicing P53/allignment scripts/IDs.txt", "r") as ins:
    array = []
    for line in ins:
        array.append(line)

for i in array:
    i = i.strip()
    with open(str(i) + ".sh", "w") as f:
        print>> f, """#!/bin/bash
#PBS -l nodes=1:ppn=32 
#PBS -l walltime=04:00:00
#PBS -l gres=ccm
#PBS -N allign_%s

module load ccm
module load hisat/0.1.6
module load samtools/1.2

cd /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams

ccmrun hisat -p 32 -q -x /N/dc2/projects/MAMMALEXP/RBP-Target-Evolution_and_Transcriptome_Dynamics/REFERENCE/Human/h38.84/h38.84 -1 /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/fastqs_GSE79249/%s_1.fastq -2 /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/fastqs_GSE79249/%s_2.fastq -S /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/%s.sam
ccmrun samtools view -S -b /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/%s.sam > /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/%s.bam
ccmrun samtools sort /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/%s.bam /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/%s.sorted
ccmrun samtools index /N/dc2/projects/CancerFight/Vidhur/P53_alternative_splicing/hisat_alignment/alligned_GEO_bams/%s.sorted.bam

""" % (str(i), str(i), str(i), str(i), str(i), str(i), str(i), str(i), str(i))

k = open("qsub_code.txt", "w")

for i in array:
    i = i.strip()
    k.write("qsub %s.sh\n" % (str(i)))

for i in array:
    i = i.strip()
    k.write("dos2unix %s.sh\n" % (str(i)))
