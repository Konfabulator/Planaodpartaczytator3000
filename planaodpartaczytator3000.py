# planaodpartaczytator3000
import subprocess

try:
    # subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    # avoid printing Requirement already satisfied:
    print("Instalowanie wymaganych bibliotek...  ", end="")
    subprocess.check_output(["pip", "install", "-r", "requirements.txt"])
    print("Done\n")
except subprocess.CalledProcessError:
    print("Nie udało się zainstalować wymaganych bibliotek. Spróbuj ręcznie zainstalować biblioteki z pliku requirements.txt")

import os
from tabulate       import tabulate
from decoder        import decode_subj_file
from plano_definder import defind_all_plans
from web_writer_v2     import get_hours
from write_class_data_to_file import write_class_data_to_file

directory = os.path.dirname(os.path.realpath(__file__)) + '//' + 'plany//'
tabelka = lambda df:tabulate(df,Kolumny,tablefmt='presto')

file_to_read = input("Wprowadź nazwę pliku z godzinami: ")                      # "Z2022_23.txt"
file_to_write = "Plany_" + file_to_read                                         # plik wyjściowy z planami zajęć
# get_hours(directory , file_to_read)                                             # tworzenie pliku wejściowego
# choose language and the university
# check if the file exists
if not os.path.isfile(directory + file_to_read):
    language = input('Choose language [pl/en]: ').strip()
    university = input('Choose university [uw/uj/uksw/...]: ').strip()
    classes_data = {}
    while True:
        print('\n###')
        Course_Code = input("Kod Przedmiotu (lub END):\n")
        Course_Code = Course_Code.strip()
        if Course_Code == 'END':
            print('\n')
            break
        
        a = get_hours((university, Course_Code), language)
        classes_data = {**classes_data, **a}
    write_class_data_to_file(directory, file_to_read, 'W', classes_data)
        
schedules = open(directory + '//'  + file_to_write, "w+", encoding="utf-8")     # gotowe plany zajęć


# Kolumny = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
Kolumny = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]
Wiersze = ['8','9','10','11','12','13','14','15','16','17','18','19','20','21']

pomijane_przedmioty = []
# pomijane_przedmioty = ["Reinforcement learning Lab","Reinforcement learning W","Analiza IV W", "Analiza IV Ć","Natural language processing Lab","Natural language processing W", "Basen","Taniec towarzyski", "Siłownia"]
godzina_start = 1

przedmioty, grupy_godz, grupy_no = decode_subj_file(file_to_read,directory)

# print(grupy_godz)
# print(grupy_no)
wykonalne_plany = defind_all_plans(przedmioty, grupy_godz, grupy_no, godzina_start, pomijane_przedmioty)

possibilities = 1
for k in range(len(przedmioty)):
    if przedmioty[k] not in pomijane_przedmioty:
        possibilities *= len(grupy_godz[k])

for i in range(len(wykonalne_plany)):
    schedules.write(str(i+1)+'.\n')
    schedules.write(tabelka(wykonalne_plany[i]))
    schedules.write("\n\n\n")
schedules.close()

print('Znaleziono '+ str(len(wykonalne_plany)) + ' z '+str(possibilities) + ' Zestawów.')
print(f'Gotowy Plan w pliku: "{file_to_write}"\n')
