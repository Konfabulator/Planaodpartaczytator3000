import os

def write_class_data_to_file(directory, file_name, write_mode, DATA):
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = directory+file_name
    # print(DATA)
    # {'Mechanika kwantowa Ćwiczenia (CW)': {'1': [['piątek', '10:15-12:00', 'B0.17'], ['poniedziałek', '13:15-15:00', '2.08']], '2': [['wtorek', '16:15-18:00', 'B0.21'], ['czwartek', '16:15-18:00', '2.24']], '3': [['piątek', '12:15-14:00', '1.38'], ['czwartek', '9:15-11:00', '1.02']], '4': [['wtorek', '9:15-11:00', '2.06'], ['czwartek', '9:15-11:00', '1.38']], '5': [['czwartek', '15:15-17:00', '1.02'], ['wtorek', '9:15-11:00', '2.03']]}, 'Mechanika kwantowa Wykład (WYK)': {'1': [['środa', '11:15-13:00', '1.01'], ['wtorek', '11:15-13:00', '1.40']]}}
    if write_mode == 'W':
        with open(directory, 'w', encoding='utf-8') as f:
            for unit in DATA.keys():
                f.write(f'"{unit}"\n')
                # print(f'"{unit}"\n')
                for group_no in DATA[unit].keys():
                    # f.write(f'{group_no} ')
                    for termin in DATA[unit][group_no]:
                        # print(termin)
                        f.write(f'{termin[0]} {termin[1]}, ')
                    f.write('\n')
                f.write('\n')