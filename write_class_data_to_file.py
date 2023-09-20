import os

def write_class_data_to_file(directory, file_name, write_mode, DATA):
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = directory+file_name
    # print(DATA)
    if write_mode == 'W':
        with open(directory, 'w', encoding='utf-8') as f:
            for unit in DATA.keys():
                f.write(f'"{unit}"\n')
                # print(f'"{unit}"\n')
                for group_no in DATA[unit].keys():
                    f.write(f'({group_no}) ')
                    for termin in DATA[unit][group_no]:
                        # print(termin)
                        f.write(f'{termin[0]} {termin[1]}, ')
                    f.write('\n')
                f.write('\n')
                
    elif write_mode == 'A':
        with open(directory, 'a', encoding='utf-8') as f:
            for unit in DATA.keys():
                f.write(f'"{unit}"\n')
                # print(f'"{unit}"\n')
                for group_no in DATA[unit].keys():
                    f.write(f'({group_no}) ')
                    for termin in DATA[unit][group_no]:
                        # print(termin)
                        f.write(f'{termin[0]} {termin[1]}, ')
                    f.write('\n')
                f.write('\n')