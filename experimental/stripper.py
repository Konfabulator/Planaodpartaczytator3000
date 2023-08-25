f = open('linki_usos_api.txt', 'r', encoding='utf-8')

for l in f.readlines():
    l = l.strip()
    if l.split(':')[1].strip() != 'None':
        print(l.split(':')[1].strip()+':'+l.split(':')[2].strip())
    else:
        print(l.split(':')[1].strip())