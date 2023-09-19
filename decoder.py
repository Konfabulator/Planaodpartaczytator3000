def decode_subj_file(file_name,directory):
    f = open(directory+file_name, "r", encoding="utf-8")
    przedmioty = []
    grupy = [[],[]]
    for line in f:
        if line[0] == '"':
            przedmioty.append(line.strip().strip('"'))
            grupy[0].append([])
            grupy[1].append([])
        elif line[0] == '(':
            a = line.replace('-',' ').split()
            print(a)
            group_no = a[0]
            a = a[1:]
            b = []
            for i in range(0,len(a),3):
                b.append([
                    int(a[i])-1,
                    int(a[i+1].partition(':')[0]),
                    int(a[i+2].partition(':')[0])
                    ])
            grupy[0][-1].append(b)
            grupy[1][-1].append(group_no)
    f.close()
    return przedmioty, grupy[0], grupy[1]