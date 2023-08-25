import os
import re
import requests
import pandas as pd
from urllib.request import urlopen
import datetime
from bs4 import BeautifulSoup

from search_by_course_code import find_course


# collect all tables from the course page
def collect_tables(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            class_title = soup.find('h1').text.split('\n')[3].strip()
        except:
            class_title = None
        return [str(table) for table in soup.find_all('table')], class_title
    else:
        return [], None

# check if the string is a date in format YYYY-MM-DD
def is_date(s):
    try:
        datetime.datetime.strptime(s, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# detect if the table contains dates interval
def has_date(s):
    if s.find(' - ') != -1:
        parts = s.split(' - ')
        for i in range(len(parts)-1):
            p1 = parts[i][-10:]
            p2 = parts[i+1][:10]
            if is_date(p1) and is_date(p2):
                # print(p1, p2)
                return p1 + ' - ' + p2
    return False

# collect groups from each class page
def collect_groups(link, language):
    groups = {}
    # collect all tables from the class page
    list_of_tables, class_title = collect_tables(link)
    a = {'pl': 'Grupa', 'en':'Group'}
    # get only tables with groups
    for t in range(len(list_of_tables)-1, -1, -1):
        if list_of_tables[t].find(a[language]) == -1:
            list_of_tables.pop(t)
    # collect group number and termins
    for table in list_of_tables:
        df = pd.read_html(table)[0]
        df = df[df[a[language]].apply(lambda x: str(x).isdigit())]
        df = df.iloc[:, :2]
        for i in range(len(df)):
            groups[df.iloc[i, 0]] = df.iloc[i, 1]
    return class_title, groups        

def split_group_data(s, language):
    room = {'pl': 'sala', 'en':'room'}
    days = {'pl': ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"],
            'en': ["monday", "tuesday", "wednesday", "thursday", "friday"]}
    # replace days with numbers
    for i in range(len(days[language])):
        s = s.replace(days[language][i], str(i+1))
    # remove rooms
    s = s.replace(f'{room[language]}', '')
    # remove spaces after commas
    while s.find(', ') != -1:
        s = s.replace(', ', ',')
    # connect days with times
    s = s.replace(' - ', '-')
    # remove spaces before every number
    for i in range(10):
        s = s.replace(f' {i}', str(i))
    # split by space
    s = s.split(' ')
    # remove empty strings
    while '' in s:
        s.remove('')
    b = []
    for i in range(len(s)):
        a = s[i].split(',')
        # a[0] = days[language][int(a[0][-1])-1]
        a[0] = int(a[0][-1])
        b.append(a)
    return b

def get_hours(class_input_data, language='pl'):
    # collect course name and url
    url, name = find_course(class_input_data[1], class_input_data[0], language)
    print(name)
    print(url)
    print()

    # remove unnecessary tables and collect dates between which the classes take place (possibly miltiple intervals - than user can choose one)
    list_of_tables, _ = collect_tables(url)
    list_of_dates = []
    for t in range(len(list_of_tables)-1, -1, -1):
        date = has_date(list_of_tables[t])
        if not date:
            list_of_tables.pop(t)
            # print('removed')
        else:
            list_of_dates.append(date)
    list_of_dates.reverse()

    # print all dates and let user choose one
    for i in range(len(list_of_dates)):
        print(f'{i+1}. {list_of_dates[i]}')
    choice = int(input('Choose date: '))-1

    # collect links to classes pages (where the groups can be collected)
    title = {'pl': 'Typ zajęć:', 'en':'Type of class:'}
    list_of_links = []
    soup = BeautifulSoup(list_of_tables[choice], 'html.parser')
    rows = soup.find_all('td')
    for row in rows:
        if row.text == title[language]:
            links = row.find_next_sibling('td').find_all('a')
            for link in links:
                list_of_links.append(link['href']+f'&lang={language}') 
    # print(list_of_links)
    groups_for_each_unit = {}
    for link in list_of_links:
        class_title, groups = collect_groups(link, language)
        groups_data = {}
        # go through all groups and collect times (convert days to numbers) and rooms
        for group in groups.keys():
            groups_data[group] = split_group_data(groups[group], language)
        # print(class_title)
        # print(groups_data)
        groups_for_each_unit[name+' '+class_title] = groups_data
    return groups_for_each_unit