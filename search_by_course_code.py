import requests
from bs4 import BeautifulSoup

def find_course(course_code, uczelnia, language='pl'):
    # USOS API
    if uczelnia == 'uw':
        url = "https://usosapps.uw.edu.pl/services/courses/course?"
    elif uczelnia == 'uj':
        url = "https://apps.usos.uj.edu.pl/services/courses/course?"
    elif uczelnia == 'pw':
        url = "https://apps.usos.pw.edu.pl/services/courses/course?"
    params = {
        "fields": "profile_url|name",
        "course_id": course_code,
    }
    data = requests.get(url, params=params).json()
    href = data['profile_url']+f'&lang={language}'
    name = ''
    if language == 'en':
        name = data['name']['en']
    else:
        name = data['name']['pl']
    return href, name