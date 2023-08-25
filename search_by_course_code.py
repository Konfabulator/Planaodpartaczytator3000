import requests
from bs4 import BeautifulSoup

def find_course(course_code, uczelnia, language='pl'):
    # USOS API
    '''
    "AMISNS" :                                                                              "amisns"
    "Akademia Nauk Stosowanych Stefana Batorego" :                                          "ansb"
    "Akademia Wychowania Fizycznego im. Bronisława Czecha w Krakowie" :                     "awf"
    "Chrześcijańska Akademia Teologiczna" :                                                 "chat"
    "Jan Dlugosz University in Czestochowa" :                                               "ujd"
    "National Academy of Dramatic Art in Warsaw" :                                          "at"
    "PWSTE w Jarosławiu" :                                                                  "pwste"
    "SGH Warsaw School of Economics" :                                                      "sgh"
    "The Academy of Fine Arts and Design in Katowice" :                                     "asp"
    "The Adam Mickiewicz University in Poznan" :                                            "amu"
    "The Bialystok School of Economics" :                                                   "wse"
    "The Bydgoszcz University of Science and Technology" :                                  "pbs"
    "The Cardinal Stefan Wyszynski University" :                                            "uksw"
    "The Cracow University of Economic" :                                                   "uek"
    "The DSW University of Lower Silesia" :                                                 "dsw"
    "The Feliks Nowowiejski Academy of Music" :                                             "amuz"
    "The Helena Chodkowska University of Law in Wrocław" :                                  "prawowroclaw"
    "The Jagiellonian University" :                                                         "uj"
    "The Jerzy Kukuczka Academy of Physical Education in Katowice" :                        "awf"
    "The Kazimierz Wielki University" :                                                     "ukw"
    "The Kielce University of Technology" :                                                 "tuk"
    "The Krosno Academy of Applied Sciences" :                                              "kpu"
    "The Military University of Technology in Warsaw" :                                     "wat"
    "The Nicolaus Copernicus University" :                                                  "umk"
    "The Opole University of Technology" :                                                  "po"
    "The Pontifical University of John Paul II" :                                           "upjp2"
    "The Poznan University of Technology" :                                                 "put"
    "The Poznań University of Economics and Business" :                                     "uep"
    "The Rzeszów University of Technology" :                                                "prz"
    "The Siedlce University of Natural Sciences and Humanities" :                           "uph"
    "The Silesian University of Technology" :                                               "polsl"
    "The Stanisław Staszic State University of Applied Sciences in Piła" :                  "ans"
    "The Technical University of Koszalin" :                                                "tu"
    "The University University of Technology and Economics" :                               "uth"
    "The University of APS" :                                                               "aps"
    "The University of Agriculture" :                                                       "ur"
    "The University of Bialystok" :                                                         "uwb"
    "The University of Euroregional Economy in Józefów - Warsaw" :                          "wsge"
    "The University of Lodz" :                                                              "ul"
    "The University of Maria Curie-Skłodowska" :                                            "umcs"
    "The University of Opole" :                                                             "uop"
    "The University of Silesia in Katowice" :                                               "us"
    "The University of Warmia and Mazury in Olsztyn" :                                      "uwm"
    "The University of Warsaw" :                                                            "uw"
    "The University of Wroclaw" :                                                           "uwr"
    "The Warsaw University of Technology" :                                                 "pw"
    "The Wroclaw University of Economics" :                                                 "uew"
    "The Wroclaw University of Science and Technology" :                                    "pwr"
    "The Wrocław University of Environmental and Life Science" :                            "upwr"
    "The president Stanisław Wojciechowski Higher Vocational State School in Kalisz" :      "pwsz"
    "University of Lomza" :                                                                 "pwsip"
    "Uniwerstytet Muzyczny Fryderyka Chopina" :                                             "chopin"
    "VISTULA UNIVERSITY" :                                                                  "vistula"
    "Wyższa Szkoła Bezpieczeństwa Publicznego i Indywidualnego „Apeiron” w Krakowie" :      "apeiron"
    '''
    if uczelnia == 'amisns':              # AMISNS
            url = 'https://usosapps.amisns.edu.pl/services/courses/course?'
    elif uczelnia == 'ansb':                # Akademia Nauk Stosowanych Stefana Batorego
            url = 'https://apps.ansb.pl/services/courses/course?'
    elif uczelnia == 'awf':                 # Akademia Wychowania Fizycznego im. Bronisława Czecha w Krakowie
            url = 'https://usosapi.awf.krakow.pl/services/courses/course?'
    elif uczelnia == 'chat':                # Chrześcijańska Akademia Teologiczna
            url = 'https://usosapps.chat.edu.pl/services/courses/course?'
    elif uczelnia == 'ujd':                 # Jan Dlugosz University in Czestochowa
            url = 'https://usosapps.ujd.edu.pl/services/courses/course?'
    elif uczelnia == 'at':                  # National Academy of Dramatic Art in Warsaw
            url = 'https://usosapps.at.edu.pl/services/courses/course?'
    elif uczelnia == 'pwste':               # PWSTE w Jarosławiu
            url = 'https://apps.pwste.edu.pl/services/courses/course?'
    elif uczelnia == 'sgh':                 # SGH Warsaw School of Economics
            url = 'https://usosapps.sgh.waw.pl/services/courses/course?'
    elif uczelnia == 'asp':                 # The Academy of Fine Arts and Design in Katowice
            url = 'https://apps.asp.katowice.pl/services/courses/course?'
    elif uczelnia == 'amu':                 # The Adam Mickiewicz University in Poznan
            url = 'https://usosapps.amu.edu.pl/services/courses/course?'
    elif uczelnia == 'wse':                 # The Bialystok School of Economics
            url = 'https://usosapps.wse.edu.pl/services/courses/course?'
    elif uczelnia == 'pbs':                 # The Bydgoszcz University of Science and Technology
            url = 'https://usosapps.pbs.edu.pl/services/courses/course?'
    elif uczelnia == 'uksw':                # The Cardinal Stefan Wyszynski University
            url = 'https://apps.usos.uksw.edu.pl/services/courses/course?'
    elif uczelnia == 'uek':                 # The Cracow University of Economic
            url = 'https://appsusos.uek.krakow.pl/services/courses/course?'
    elif uczelnia == 'dsw':                 # The DSW University of Lower Silesia
            url = 'https://usosapps.dsw.edu.pl/services/courses/course?'
    elif uczelnia == 'amuz':                # The Feliks Nowowiejski Academy of Music
            url = 'https://www.usosapi.amuz.bydgoszcz.pl/services/courses/course?'
    elif uczelnia == 'prawowroclaw':        # The Helena Chodkowska University of Law in Wrocław
            url = 'https://apps.prawowroclaw.edu.pl/services/courses/course?'
    elif uczelnia == 'uj':                  # The Jagiellonian University
            url = 'https://apps.usos.uj.edu.pl/services/courses/course?'
    elif uczelnia == 'awf':                 # The Jerzy Kukuczka Academy of Physical Education in Katowice
            url = 'https://usosapps.awf.katowice.pl/services/courses/course?'
    elif uczelnia == 'ukw':                 # The Kazimierz Wielki University
            url = 'https://api.ukw.edu.pl/services/courses/course?'
    elif uczelnia == 'tuk':                 # The Kielce University of Technology
            url = 'https://api.usos.tu.kielce.pl/services/courses/course?'
    elif uczelnia == 'kpu':                 # The Krosno Academy of Applied Sciences
            url = 'https://usosapps.kpu.krosno.pl/services/courses/course?'
    elif uczelnia == 'wat':                 # The Military University of Technology in Warsaw
            url = 'https://usosapps.wat.edu.pl/services/courses/course?'
    elif uczelnia == 'umk':                 # The Nicolaus Copernicus University
            url = 'https://usosapps.umk.pl/services/courses/course?'
    elif uczelnia == 'po':                  # The Opole University of Technology
            url = 'https://usosapps.po.edu.pl/services/courses/course?'
    elif uczelnia == 'upjp2':               # The Pontifical University of John Paul II
            url = 'https://usosapi.upjp2.edu.pl/services/courses/course?'
    elif uczelnia == 'put':                 # The Poznan University of Technology
            url = 'https://usosapps.put.poznan.pl/services/courses/course?'
    elif uczelnia == 'uep':                 # The Poznań University of Economics and Business
            url = 'https://usosapps.ue.poznan.pl/services/courses/course?'
    elif uczelnia == 'prz':                 # The Rzeszów University of Technology
            url = 'https://usosapps.prz.edu.pl/services/courses/course?'
    elif uczelnia == 'uph':                 # The Siedlce University of Natural Sciences and Humanities
            url = 'https://apps.uph.edu.pl/services/courses/course?'
    elif uczelnia == 'polsl':               # The Silesian University of Technology
            url = 'https://usosapi.polsl.pl/services/courses/course?'
    elif uczelnia == 'ans':                 # The Stanisław Staszic State University of Applied Sciences in Piła
            url = 'https://usosapi.ans.pila.pl/services/courses/course?'
    elif uczelnia == 'tu':                  # The Technical University of Koszalin
            url = 'https://usosapi.tu.koszalin.pl/services/courses/course?'
    elif uczelnia == 'uth':                 # The University University of Technology and Economics
            url = 'https://usosapps.uth.edu.pl/services/courses/course?'
    elif uczelnia == 'aps':                 # The University of APS
            url = 'https://apps.aps.edu.pl/services/courses/course?'
    elif uczelnia == 'ur':                  # The University of Agriculture
            url = 'https://usosapi.ur.krakow.pl/services/courses/course?'
    elif uczelnia == 'uwb':                 # The University of Bialystok
            url = 'https://usosapps.uwb.edu.pl/services/courses/course?'
    elif uczelnia == 'wsge':                # The University of Euroregional Economy in Józefów - Warsaw
            url = 'https://usosapi.wsge.edu.pl/services/courses/course?'
    elif uczelnia == 'ul':                  # The University of Lodz
            url = 'https://usosapps.uni.lodz.pl/services/courses/course?'
    elif uczelnia == 'umcs':                # The University of Maria Curie-Skłodowska
            url = 'https://apps.umcs.pl/services/courses/course?'
    elif uczelnia == 'uop':                 # The University of Opole
            url = 'https://usosapps.uni.opole.pl/services/courses/course?'
    elif uczelnia == 'us':                  # The University of Silesia in Katowice
            url = 'https://usosapps.us.edu.pl/services/courses/course?'
    elif uczelnia == 'uwm':                 # The University of Warmia and Mazury in Olsztyn
            url = 'https://apps.uwm.edu.pl/services/courses/course?'
    elif uczelnia == 'uw':                  # The University of Warsaw
            url = 'https://usosapps.uw.edu.pl/services/courses/course?'
    elif uczelnia == 'uwr':                 # The University of Wroclaw
            url = 'https://usosapps.uni.wroc.pl/services/courses/course?'
    elif uczelnia == 'pw':                  # The Warsaw University of Technology
            url = 'https://apps.usos.pw.edu.pl/services/courses/course?'
    elif uczelnia == 'uew':                 # The Wroclaw University of Economics
            url = 'https://usosapps.ue.wroc.pl/services/courses/course?'
    elif uczelnia == 'pwr':                 # The Wroclaw University of Science and Technology
            url = 'https://apps.usos.pwr.edu.pl/services/courses/course?'
    elif uczelnia == 'upwr':                # The Wrocław University of Environmental and Life Science
            url = 'https://usosapps.upwr.edu.pl/services/courses/course?'
    elif uczelnia == 'pwsz':                # The president Stanisław Wojciechowski Higher Vocational State School in Kalisz
            url = 'https://apps.pwsz.kalisz.pl/services/courses/course?'
    elif uczelnia == 'pwsip':               # University of Lomza
            url = 'https://api.pwsip.edu.pl/usosapps/services/courses/course?'
    elif uczelnia == 'chopin':              # Uniwerstytet Muzyczny Fryderyka Chopina
            url = 'https://usosapps.chopin.edu.pl/services/courses/course?'
    elif uczelnia == 'vistula':             # VISTULA UNIVERSITY
            url = 'https://usosapps.vistula.edu.pl/services/courses/course?'
    elif uczelnia == 'apeiron':             # Wyższa Szkoła Bezpieczeństwa Publicznego i Indywidualnego „Apeiron” w Krakowie
            url = 'https://usosapi.apeiron.edu.pl/services/courses/course?'
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