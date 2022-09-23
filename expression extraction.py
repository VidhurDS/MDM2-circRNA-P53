# Opening input files for TCGA IDs and filenames
with open("filenames.txt", "r") as ins:
    filenames = []
    for line in ins:
        filenames.append(line.strip())
ins.close()

out = open("expression_MATR3_TP53.txt", 'w')
# change address
# address = "E:/Academic SoIC/SCJ/Dr. Ashish Lal/question 1/expression matrix from CancerFight/sample data folder/"
address = "/N/dc2/projects/CancerFight/COAD_Collaboration/Gene_Level/"

for name in filenames:
    name = name.strip()
    num = int(name[13:15])
    if num < 10:                # filtering only tumor files
        full_name = address+name
        full_file = []
        with open(full_name, "r") as ins:
            full_file = ins.readlines()
        ins.close()
        out_line = ''
        for ensg in full_file:
            ensg = ensg.strip()
            ele = []
            if ensg.startswith(("ENSG00000015479","ENSG00000280987","ENSG00000141510")):
                ele = ensg.split("\t")
                unit = "\t"+ele[0]+"||"+ele[1]+"||"+ele[8]
                out_line += unit
        out.write(name[0:12]+out_line+"\n")
