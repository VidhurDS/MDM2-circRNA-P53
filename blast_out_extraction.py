# Opening input files for TCGA IDs and filenames
with open("blast_out_filenames.txt", "r") as ins:
    filenames = []
    for line in ins:
        filenames.append(line.strip())
ins.close()

out = open("extracted_blast_out.txt", 'w')
# change address
address = "E:/Academic SoIC/SCJ/Dr. Ashish Lal/circMDM2/30nt BLAST/analysis/blast_out/"
# address = "/N/dc2/projects/CancerFight/COAD_Collaboration/Gene_Level/"

out.write("query_id\tsubject_id\tq._start\tq._end\tquery_seq\tsubject_seq\tevalue\talignment_length\t%_identity\tidentical\tgap_opens\tgaps\t%_subject_coverage\t%_hsp_coverage\n")

full_file = []

for name in filenames:
    name = name.strip()
    full_name = address + name
    with open(full_name, "r") as fins:
        for line in fins:
            if line[0] != '#':
                full_file.append(line.strip())
    ins.close()

for event in full_file:
    out.write(event+"\n")

# full_file = fins.readlines()
#    num = int(name[13:15])
#    if num < 10:                # filtering only tumor files
#        full_name = address+name
#        full_file = []
#        with open(full_name, "r") as ins:
#            full_file = ins.readlines()
#        ins.close()
#        for ensg in full_file:
#            ensg = ensg.strip()
#            ele = []
#            if ensg.startswith("ENSG00000250337"):
#                ele = ensg.split("\t")
#                out.write(name[0:12]+"\t"+ele[0]+"\t"+ele[1]+"\t"+ele[8]+"\n")
