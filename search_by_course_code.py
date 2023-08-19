import requests
from bs4 import BeautifulSoup

def find_course(course_code, language='pl'):
    # USOS API
    url = "https://usosapps.uw.edu.pl/services/courses/course?"
    params = {
        "fields": "profile_url|name",
        "course_id": "1100-2AF23",
    }
    data = requests.get(url, params=params).json()
    href = data['profile_url']
    if language == 'en':
        name = data['name']['en']
    else:
        name = data['name']['pl']
    return href, name