# Opening input files for TCGA IDs and filenames
with open("filenames.txt", "r") as ins:
    filenames = []
    for line in ins:
        filenames.append(line.strip())
ins.close()

out = open("files_with_PINCR_expression.txt", 'w')
# change address
# address = "E:/Academic SoIC/SCJ/Dr. Ashish Lal/question 3/"
address = "/N/dc2/projects/CancerFight/COAD_Collaboration/Gene_Level/"

out.write("File_name\tID_form\n")

for name in filenames:
    name = name.strip()
    num = int(name[13:15])
    if num < 10:                # filtering only tumor files
        full_name = address+name
        full_file = []
        with open(full_name, "r") as ins:
            full_file = ins.readlines()
        ins.close()
        for ensg in full_file:
            ensg = ensg.strip()
            if ('PINCR' in ensg) or ('RP3-326I13.1' in ensg) or ('ENSG00000224294' in ensg):
                out.write(name+"\t"+ensg+"\n")
                print (name+"\t"+ensg+"\n")
