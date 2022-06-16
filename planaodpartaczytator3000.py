# planaodpartaczytator3000
import os
from tabulate       import tabulate
from decoder        import decode_subj_file
from plano_definder import defind_all_plans

directory = os.path.dirname(os.path.realpath(__file__)) + '//'
tabelka = lambda df:tabulate(df,Kolumny,tablefmt='presto')

file_to_read = input("Wprowadź nazwę pliku z godzinami")                        #"Z2022_23.txt"
file_to_write = "Plany_" + file_to_read                                         # plik wyjściowy z planami zajęć
schedules = open(directory + '\\'  + file_to_write, "w+", encoding="utf-8")     # gotowe plany zajęć

Kolumny = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
Wiersze = ['8','9','10','11','12','13','14','15','16','17','18']

pomijane_przedmioty = ["Migowy","Niemiecki"]#,"Hiszpański"
godzina_start = 8

przedmioty, grupy = decode_subj_file(file_to_read,directory)
wykonalne_plany = defind_all_plans(przedmioty, grupy, godzina_start, pomijane_przedmioty)

possibilities = 1
for k in range(len(przedmioty)):
    if przedmioty[k] not in pomijane_przedmioty:
        possibilities *= len(grupy[k])

print('Znaleziono '+ str(len(wykonalne_plany)) + ' z '+str(possibilities) + ' Zestawów.')

for i in range(len(wykonalne_plany)):
    schedules.write(str(i+1)+'.\n')
    schedules.write(tabelka(wykonalne_plany[i]))
    schedules.write("\n\n\n")
