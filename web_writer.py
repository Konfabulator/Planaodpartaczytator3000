import os
import re
import requests
import pandas as pd
from urllib.request import urlopen

from search_by_course_code import find_course

dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]

def get_page_title(html_page, title = "title"):
    for i in range(len(html_page)):
        if "<title>" in html_page[i]:
            return(html_page[i].split('-')[0].strip()[7:])
            
def Read_subj_page(url):
    # print(url+'\n\n')
    html = urlopen(url).read().decode("utf-8").splitlines()
    page_title = get_page_title(html)
    
    classes_links = []
    classes_names = []
    
    df = pd.read_html(requests.get(url).content)[-1]
    classes_names = df[1][1].split('więcej informacji')
    
    for i in range(len(classes_names)):
        classes_names[i] = page_title+' '+classes_names[i].strip(" ").split(',')[0]
        
    
    for i in range(len(html)-1, -1, -1):
        if "Typ zajęć" in html[i]:
            for j in range(i,len(html)):
                if 'href' in html[j]:
                    classes_links.append(re.search("(?P<url>https?://[^\s]+)", html[j]).group("url"))
                if 'Koordynatorzy' in html[j]:
                    break
            break
    return page_title, classes_names, classes_links

def Read_website(url, subject=True):
    course_name, classes_names, classes_links = Read_subj_page(url)
    classes = []
    for u in range(len(classes_links)):
        classes.append([])
        df = pd.read_html(requests.get(classes_links[u]).content)[-1]
        grupy = df.values.tolist()[:-1]
        for i in grupy:
            classes[-1].append([])
            grupa = i[1].split(',')
            for zaj in range(0,len(grupa),2):
                for j in range(len(dni)):
                    if dni[j] in grupa[zaj]:
                        hours = grupa[zaj+1]
                        classes[-1][-1].append(str(j+1)+hours)
                        zaj += 2
                        break
    return course_name, classes, classes_names

def get_hours(directory, file_name):
    # check if plany folder exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    directory = directory+file_name
    # check if file exists
    if os.path.isfile(directory):
        print("Plik już istnieje.\n")
    ReadOrWrite = input('Read/Write/Append [R/W/A]: ')
    if  ReadOrWrite.upper() == 'W' or ReadOrWrite.upper() == 'A':
        if ReadOrWrite.upper() == 'W':
            plik_z_grupami = open(directory, "w+", encoding="utf-8")
        else:
            plik_z_grupami = open(directory, "a+", encoding="utf-8")
        zetonowe = False
        while True:
            if zetonowe == False:
                Course_Code = input("Kod Przedmiotu (lub END):\n")
                Course_Code = Course_Code.strip()                
            if Course_Code == 'END':
                print('\n')
                break
            Course_Url = find_course(Course_Code)
            course_name, classes, classes_names = Read_website(Course_Url, not zetonowe)
            for i in range(len(classes)):
                if classes[i] == [[]]:
                    print('Brak godzin w grupie '+classes_names[i])
                else:
                    plik_z_grupami.write('"'+classes_names[i]+'"\n')
                    for j in classes[i]:
                        if_was = False
                        for k in j:
                            if if_was == True:
                                plik_z_grupami.write(', ')
                            plik_z_grupami.write(k)
                            if_was = True
                        plik_z_grupami.write('\n')
                    plik_z_grupami.write('\n')
            plik_z_grupami.flush()
            print(f'Pobrano dane grup zajęciowych przedmiotu "{course_name}"\n')
            
        plik_z_grupami.close()