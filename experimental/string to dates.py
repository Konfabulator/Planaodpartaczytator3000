'''
string = "każdy poniedziałek, 8:00 - 9:00, sala basen duży"
dates = [[1, "8:00-9:00"]]

string = "każdy wtorek, 9:00 - 14:00, sala Pasteura, III piętro każdy czwartek, 14:00 - 18:00, sala Pasteura, III piętro"
dates = [[2, "9:00-14:00"], [4, "14:00-18:00"]]

string = "every Wednesday, 12:15 - 14:00, room 2.03 every Monday, 15:15 - 17:00, room 2.23"
dates = [[3, "12:15-14:00"], [1, "15:15-17:00"]]

string = "każda środa, 14:15 - 16:00, sala 1.38 każdy piątek, 9:15 - 11:00, sala 2.24"
dates = [[3, "14:15-16:00"], [5, "9:15-11:00"]]

string = "każdy piątek, 11:15 - 14:00, sala 1.01"
dates = [[5, "11:15-14:00"]]
'''
# write python code that will input the 'string' and return 'dates' list in the way that is shown above
# you can use any python libraries you want

def split_group_data(s, language):
    days = {'pl': ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"],
            'en': ["monday", "tuesday", "wednesday", "thursday", "friday"]}
    groups = []
    s = s.lower()
    words = s.split(' ')
    for i in range(len(words)):
        word = words[i]
        for d in days[language]:
            if d in word:
                a = [d, '']
                for j in range(i + 1, len(words)):
                    word = words[j]
                    print(word)
                    if word == ' ':
                        continue
                    if word[0].isdigit():
                        a[1] += word
                    elif word[0] in [':', '-']:
                        a[1] += word
                    else:
                        break
                # remove unwanted characters
                for i in range(len(a[1])-1, -1, -1):
                    if a[1][i] not in [' ', ':', '-'] and not a[1][i].isdigit():
                        a[1] = a[1][:i] + a[1][i+1:]
                groups.append(a)
    dates = []
    for group in groups:
        day = group[0]
        times = group[1].split(day)
        for time in times:
            if time != '':
                dates.append([days[language].index(day) + 1, time.strip()])
    return dates
    
    
lang = 'en'
string = "every Wednesday, 12:15 - 14:00, room 2.03 every Monday, 15:15 - 17:00, room 2.23"
# string = "każda środa, 14:15 - 16:00; sala 1.38 każdy piątek, 9:15 - 11:00, sala 2.24"
groups = split_group_data(string, lang)
print(groups)