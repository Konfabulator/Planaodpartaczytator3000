import requests
from bs4 import BeautifulSoup

def find_course(course_code, language='pl'):
    # polish
    if language == 'pl':
        url = 'http://informatorects.uw.edu.pl/pl/courses/view?prz_kod=' + course_code
    else:
        url = 'http://informatorects.uw.edu.pl/en/courses/view?prz_kod=' + course_code
    # open url
    r = requests.get(url)
    # get html
    html = r.text
    # parse html
    soup = BeautifulSoup(html, 'html.parser')
    # open last link on the page
    link = soup.find_all('a')[-1]
    # get href
    href = link.get('href')
    return href