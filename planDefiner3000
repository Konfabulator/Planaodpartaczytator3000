# schedulecreator3000
import os
from tabulate       import tabulate
from decoder        import decode_subj_file
from planFinder  import define_all_plans
from webWriter     import get_hours
directory = os.path.dirname(os.path.realpath(__file__)) + '//'
table = lambda df:tabulate(df,Columns,tablefmt='presto')

file_to_read = input("Enter file name with hours: ")                      # "Z2022_23.txt"
file_to_write = "Schedules_" + file_to_read                                         # output file with schedules
get_hours(directory + '//'  + file_to_read)                                     # creating an input file
schedules = open(directory + '//'  + file_to_write, "w+", encoding="utf-8")     # ready schedules


Columns = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
Rows = ['8','9','10','11','12','13','14','15','16','17','18']

excluded_subjects = []
start_hour = 1

subjects, groups = decode_subj_file(file_to_read,directory)
executable_schedules = define_all_plans(subjects, groups, start_hour, excluded_subjects)

possibilities = 1
for k in range(len(subjects)):
    if subjects[k] not in excluded_subjects:
        possibilities *= len(groups[k])

print('Found '+ str(len(executable_schedules)) + ' out of '+str(possibilities) + ' Sets.')

for i in range(len(executable_schedules)):
    schedules.write(str(i+1)+'.\n')
    schedules.write(table(executable_schedules[i]))
    schedules.write("\n\n\n")
