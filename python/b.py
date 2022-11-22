import csv
with open("c19.csv",'r') as cfile:
    vfile=csv.DictReader(cfile)
    # for line in vfile:
    #     for line1 in range(len(line)):
    #             print(line1)
    #             break
    row=list(vfile)
    max =0
    for i in range(len(row)):
        if(max<len(row[i])):
            max=len(row[i])

    p = len(row)
    print(p,max)
    print(row[3])
    