# planaodpartaczytator3000
import subprocess
import os, sys
os.chdir(os.path.dirname(os.path.realpath(__file__)))


try:
    # subprocess.check_call(["pip", "install", "-r", "requirements.txt"])
    # avoid printing Requirement already satisfied:
    print("Instalowanie wymaganych bibliotek...  ", end="")
    subprocess.check_output(["pip", "install", "-r", "requirements.txt"])
    print("Done\n")
except subprocess.CalledProcessError:
    print("Nie udało się zainstalować wymaganych bibliotek. Spróbuj ręcznie zainstalować biblioteki z pliku requirements.txt")

from time          import sleep
from tabulate       import tabulate
from decoder        import decode_subj_file
from plano_definder import defind_all_plans
from web_writer_v2     import get_hours
from write_class_data_to_file import write_class_data_to_file

directory = os.path.dirname(os.path.realpath(__file__)) + '//' + 'plany//'
tabelka = lambda df:tabulate(df,Kolumny,tablefmt='presto')

language = input('Choose language [pl/en]: ').strip()

if language == 'pl':
    file_to_read = input("Wprowadź nazwę pliku z godzinami (dowolna nazwa/już utworzony plik & np.:nowy_plan): ")                      # "Z2022_23.txt"
else:
    file_to_read = input("Enter the name of the file with hours (any name/already created file): ")                      # "Z2022_23.txt"

if file_to_read[-4:] != '.txt':
    file_to_read += '.txt'
    
file_to_write = "Plany_" + file_to_read                                         # plik wyjściowy z planami zajęć
# get_hours(directory , file_to_read)                                             # tworzenie pliku wejściowego
# choose language and the university
# check if the file exists
file_operation_type = os.path.isfile(directory + file_to_read)
if file_operation_type:
    if language == 'pl':
        a = input('Plik "' + file_to_read + '" już istnieje. Nadpisać Dane[N]/Dopisać Dane[D]/Wygenerować Plany? [N/D/W]: ').strip().upper()
    else:
        a = input('File "' + file_to_read + '" already exists. Overwrite Data[O]/Append Data[A]/Generate Plans? [O/A/G]: ').strip().upper()
            
    if a == 'N' or a == 'O':
        file_operation_type = 'W'
    elif a == 'D' or a == 'A':
        file_operation_type = 'A'
    else:
        file_operation_type = 'G'
else:
    file_operation_type = 'W'

if file_operation_type != 'G':
    if language == 'pl':
        university = input('Wybierz uniwersytet [uw/uj/uksw/...]: ').strip()
    else:
        university = input('Choose university [uw/uj/uksw/...]: ').strip()
        
    classes_data = {}
    while True:
        print('\n###')
        if language == 'pl':
            Course_Code = input('Wprowadź kod przedmiotu (lub END): ').strip()
        else:
            Course_Code = input('Enter the course code (or END): ').strip()
            
        if Course_Code.upper() == 'END':
            print('\n')
            break
        
        a = get_hours((university, Course_Code), language)
        if a:
            classes_data = {**classes_data, **a}
        else:
            if language == 'pl':
                print('Anulowano dodanie przedmiotu\n')
            else:
                print('Canceled adding the course\n')
    
    write_class_data_to_file(directory, file_to_read, file_operation_type, classes_data)
        
schedules = open(directory + '//'  + file_to_write, "w+", encoding="utf-8")     # gotowe plany zajęć


# Kolumny = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
if language == 'pl':
    Kolumny = ["Poniedziałek", "Wtorek", "Środa", "Czwartek", "Piątek"]
else:
    Kolumny = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

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

if language == 'pl':
    print('Znaleziono '+ str(len(wykonalne_plany)) + ' z '+str(possibilities) + ' Zestawów.')
    print(f'Gotowy Plan w pliku: "{file_to_write}"\n')
else:
    print('Found '+ str(len(wykonalne_plany)) + ' out of '+str(possibilities) + ' Schedules.')
    print(f'Finished Schedule in file: "{file_to_write}"\n')

print('\n\n')
# stop terminal window from closing
if language == 'pl':
    print('Aby zamknąć to okno naciśnij Enter...')
else:
    print('Press Enter to close this window...')
input()
