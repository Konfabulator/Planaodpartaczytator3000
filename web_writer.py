import os
import re
import requests
import pandas as pd
from urllib.request import urlopen
dni = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"]

def get_title(html_page, title = "title"):
    # page_title = ''
    # if title=="title":
        for i in range(len(html_page)):
            if "<title>" in html_page[i]:
                return(html_page[i].split('-')[0].strip()[7:])
                # break
    # else:
    #     for i in range(len(html_page)):
    #         # print(html_page[i])
    #         if f'<{title}>' in html_page[i]:
    #             return html_page[i]
    #             # return(html_page[i].split('-')[0].strip()[7:])
def Read_subj_page(url):
    print(url+'\n\n\n\n')
    html = urlopen(url).read().decode("utf-8").splitlines()
    page_title = get_title(html)

    classes_links = []
    classes_names = []
    
    df = pd.read_html(requests.get(url).content)[-1]
    classes_names = df[1][1].split('więcej informacji')
    # print(df[1][1].split('więcej informacji'))
    # print(classes_names.pop(-1))
    for i in range(len(classes_names)):
        classes_names[i] = page_title+' '+classes_names[i].strip(" ").split(',')[0]
    # print(classes_names)
    for i in range(len(html)-1, -1, -1):
        if "Typ zajęć" in html[i]:
            for j in range(i,len(html)):
                # print(html[j])
                if 'href' in html[j]:
                    # classes_names.append(page_title+' '+html[j].split()[0][:-1])
                    classes_links.append(re.search("(?P<url>https?://[^\s]+)", html[j]).group("url"))
                if 'Koordynatorzy' in html[j]:
                    break
            break
    return classes_names, classes_links

def Read_website(url, subject=True):
    # html = urlopen(url).read().decode("utf-8").splitlines()
    # classes_names, classes_links = [],[]
    # if subject:
    classes_names, classes_links = Read_subj_page(url)
    # else:
    #     classes_names = [get_title(html)]
    #     classes_links = [url]
    classes = []
    # print(classes_links)
    for u in range(len(classes_links)):
        # print(get_title(urlopen(classes_links[u]).read().decode("utf-8").splitlines(),"h1"))
        classes.append([])
        df = pd.read_html(requests.get(classes_links[u]).content)[-1]
        grupy = df.values.tolist()[:-1]
        # print(df)
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
    return classes, classes_names

def get_hours(directory):
    if input('Read/Write [R/W]: ') == 'W':
        plik_z_grupami = open(directory, "w+", encoding="utf-8")
        zetonowe = False
        while True:
            if zetonowe == False:
                Url = input("Link do strony przedmiotu (lub END):\n")
            if Url == 'END':
                # zetonowe = True
                break
            # if zetonowe == True:
            #     Url = input("Link do strony zajęć (lub END):\n")
            a, b = Read_website(Url,not zetonowe)
            # print(a)
            for i in range(len(a)):
                plik_z_grupami.write('"'+b[i]+'"\n')
                for j in a[i]:
                    if_was = False
                    for k in j:
                        if if_was == True:
                            plik_z_grupami.write(', ')
                        plik_z_grupami.write(k)
                        if_was = True
                    plik_z_grupami.write('\n')
                plik_z_grupami.write('\n')
            plik_z_grupami.flush()
            # os.fsync(plik_z_grupami.fileno())

        plik_z_grupami.close()