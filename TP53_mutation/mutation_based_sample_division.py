f = open("TCGA_IDs_with_tp53_mutation.txt",'r')
tp53_mut = f.readlines()[1:]
f.close()

a = open("all_TCGA_patient_IDs_cBioPortal.txt",'r')
all_id = a.readlines()[1:]
a.close()

M = open("event_expression_MATR3.txt",'r')
matr3_exp = M.readlines()[1:]
M.close()

out_m = open("event_expression_MATR3_tp53_mutated.txt", 'w')
out_n = open("event_expression_MATR3_tp53_wild_type.txt", 'w')

out_m.write("TCGA_ID\tEvent\tTime\tGroup\n")
out_n.write("TCGA_ID\tEvent\tTime\tGroup\n")

tp_arr = {}
tp_mut = {}
clean_all_ids = []
clean_tp53_mut = []

for each in tp53_mut:
    each = each.strip()
    clean_tp53_mut.append(each)

for aeach in all_id:
    aeach = aeach.strip()
    clean_all_ids.append(aeach)
    if aeach in clean_tp53_mut:
        tp_mut[aeach] = 1
        # print aeach
    else:
        tp_mut[aeach] = 0

for each_line in matr3_exp:
    each_line = each_line.strip()
    each_line_elemets = []
    each_line_elemets = each_line.split("\t")
    if each_line_elemets[0] in clean_all_ids:
        # print each_line_elemets[0]
        if tp_mut[each_line_elemets[0]] == 1:
            out_m.write(each_line+"\n")
        elif tp_mut[each_line_elemets[0]] == 0:
            out_n.write(each_line+"\n")
