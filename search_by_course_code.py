import requests
from bs4 import BeautifulSoup

def find_course(course_code, uczelnia, language='pl'):
    # USOS API
    '''
    Udziałowcy MUCI:
    Uniwersytet im. Adama Mickiewicza w Poznaniu
    Uniwersytet Jagielloński
    Uniwersytet Kardynała Stefana Wyszyńskiego
    Uniwersytet Kazimierza Wielkiego
    Uniwersytet Łódzki
    Uniwersytet Marii Curie-Skłodowskiej
    Uniwersytet Mikołaja Kopernika w Toruniu
    Uniwersytet Opolski
    Uniwersytet Śląski
    Uniwersytet w Białymstoku
    Uniwersytet Warmińsko-Mazurski
    Uniwersytet Warszawski
    Uniwersytet Wrocławski
    '''
    if uczelnia == 'uam':           # Uniwersytet Adama Mickiewicza w Poznaniu
        url = "https://usosapps.amu.edu.pl/services/courses/course?"
    elif uczelnia == 'uj':          # Uniwersytet Jagielloński                  TESTED
        url = "https://apps.usos.uj.edu.pl/services/courses/course?"
    elif uczelnia == 'uksw':        # Uniwersytet Kardynała Stefana Wyszyńskiego
        url = "https://apps.usos.uksw.edu.pl/services/courses/course?"
    elif uczelnia == 'ukw':         # Uniwersytet Kazimierza Wielkiego
        url = "https://api.ukw.edu.pl/services/courses/course?"
    elif uczelnia == 'ul':          # Uniwersytet Łódzki
        url = "https://usosapps.uni.lodz.pl/services/courses/course?"
    elif uczelnia == 'umcs':        # Uniwersytet Marii Curie-Skłodowskiej
        url = "https://apps.umcs.pl/services/courses/course?"
    elif uczelnia == 'uwm':         # Uniwersytet Warmińsko-Mazurski
        url = "https://apps.uwm.edu.pl/services/courses/course?"
    elif uczelnia == 'uop':         # Uniwersytet Opolski
        url = "https://usosapps.uni.opole.pl/services/courses/course?"
    elif uczelnia == 'us':          # Uniwersytet Śląski
        url = "https://usosapps.us.edu.pl/services/courses/course?"
    elif uczelnia == 'ub':          # Uniwersytet w Białymstoku
        url = "https://usosapps.uwb.edu.pl/services/courses/course?"
    elif uczelnia == 'uw':          # Uniwersytet Warszawski                    TESTED
        url = "https://usosapps.uw.edu.pl/services/courses/course?"
    elif uczelnia == 'uwr':         # Uniwersytet Wrocławski
        url = "https://usosapps.uni.wroc.pl/services/courses/course?"
    else:
        return None, None
        
        
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