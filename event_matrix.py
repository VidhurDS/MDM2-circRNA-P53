with open("clinical_patient_coad.txt", "r") as ins:
    clinical = []
    for line in ins:
        clinical.append(line.strip())
ins.close()

with open("expression_MATR3_TP53.txt", "r") as eins:
    exp = []
    for line in eins:
        exp.append(line.strip())
eins.close()

out = open("event_expression_MATR3_TP53.txt", 'w')

vital_status = {}
time = {}

for each_case in clinical:
    each_case = each_case.strip()
    each_case_elements = each_case.split("\t")
    if each_case_elements[1] == 'Alive':
        vital_status[each_case_elements[0]] = 0
    elif each_case_elements[1] == 'Dead':
        vital_status[each_case_elements[0]] = 1

    if each_case_elements[2].isdigit():
        time[each_case_elements[0]] = each_case_elements[2]
    elif each_case_elements[3].isdigit():
        time[each_case_elements[0]] = each_case_elements[3]

out.write("TCGA_ID\tVital_status\tTime\tMATR3/ENSG00000015479_TPM\tMATR3/ENSG00000280987_TPM\tTP53/ENSG00000141510_TPM\n")

for each_line in exp:
    each_line = each_line.strip()
    each_line_elemets = []
    each_line_elemets = each_line.split("\t")
    if each_line_elemets[0] in vital_status and each_line_elemets[0] in time:
        for ind in each_line_elemets:
            vals = []
            vals = ind.split("||")
            if vals[0] == "ENSG00000141510":
                tp = vals[2]
            elif vals[0] == "ENSG00000015479":
                m1 = vals[2]
            elif vals[0] == "ENSG00000280987":
                m2 = vals[2]
        fin = "\t"+m1+"\t"+m2+"\t"+tp+"\n"
        out.write(each_line_elemets[0]+"\t"+str(vital_status[each_line_elemets[0]])+"\t"+str(time[each_line_elemets[0]]))
        out.write(fin)
