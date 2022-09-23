with open("old_event_expression_MATR3_TP53.txt", "r") as eins:
    exp = []
    for line in eins:
        exp.append(line.strip())
eins.close()

out_m = open("event_expression_MATR3.txt", 'w')
out_t = open("event_expression_TP53.txt", 'w')

out_m.write("TCGA_ID\tEvent\tTime\tGroup\n")
out_t.write("TCGA_ID\tEvent\tTime\tGroup\n")

for each_line in exp:
    each_line = each_line.strip()
    each_line_elemets = []
    each_line_elemets = each_line.split("\t")
    if float(each_line_elemets[4]) >= float(20.77107):
        out_m.write(each_line_elemets[0]+"\t"+str(each_line_elemets[1])+"\t"+str(each_line_elemets[2])+"\t"+"HIGH\n")
    elif float(each_line_elemets[4]) < float(20.77107):
        out_m.write(each_line_elemets[0]+"\t"+str(each_line_elemets[1])+"\t"+str(each_line_elemets[2])+"\t"+"LOW\n")

    if float(each_line_elemets[5]) >= float(int(57.9118)):
            out_t.write(each_line_elemets[0]+"\t"+str(each_line_elemets[1])+"\t"+str(each_line_elemets[2])+"\t"+"HIGH\n")
    elif float(each_line_elemets[4]) < float(57.9118):
            out_t.write(each_line_elemets[0]+"\t"+str(each_line_elemets[1])+"\t"+str(each_line_elemets[2])+"\t"+"LOW\n")

