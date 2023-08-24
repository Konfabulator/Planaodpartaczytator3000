import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import requests
import datetime
from bs4 import BeautifulSoup
from search_by_course_code import find_course
import pandas as pd

kod = '1100-2AF23'#"WSM.IASP-KON1-24" #
language = 'en'
days = {'pl': ["poniedziałek", "wtorek", "środa", "czwartek", "piątek"], 
        'en': ["monday", "tuesday", "wednesday", "thursday", "friday"]}

# collect course name and url
url, name = find_course(kod, 'uw', language)
print(url, name)

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
        # print("Error:", response.status_code)
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
                print(p1, p2)
                return p1 + ' - ' + p2
    return False

# remove unnecessary tables and collect dates between which the classes take place (possibly miltiple intervals - than user can choose one)
list_of_tables, _ = collect_tables(url)
list_of_dates = []
for t in range(len(list_of_tables)-1, -1, -1):
    date = has_date(list_of_tables[t])
    if not date:
        list_of_tables.pop(t)
        print('removed')
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
print(list_of_links)

# collect groups from each class page
for link in list_of_links:
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
    print(class_title)
    print(groups)
        
    
    
'''

<!DOCTYPE html>
<html lang="pl">
    <head>
        <title>Semestr letni 2022/23 - Ćwiczenia (CW) - USOSweb Wydziału Fizyki UW</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
        <meta name="deklaracja-dostępności" content="https://usosweb.fuw.edu.pl/kontroler.php?_action=news/deklaracjaDostepnosci">
        <link rel="shortcut icon" href="https://usosweb.fuw.edu.pl/favicon.ico">
                
            <style id="antiClickjack">body{display:none !important;}</style>
            <script>
               if (self === top) {
                   var antiClickjack = document.getElementById("antiClickjack");
                   antiClickjack.parentNode.removeChild(antiClickjack);
               } else {
                   top.location = self.location;
               }
            </script>
        
        <script>
                        JSGLOBALS = {
                user_id: "414296",
                action: "katalog2/przedmioty/pokazGrupyZajec"
            };
            sys_www_path = "https://usosweb.fuw.edu.pl/";
            lang = "pl";
            csrftoken = "2023-08-24-67e22843eaff6155";
            debugMode = false;
        </script>
        <link rel='stylesheet' href='https://usosweb.fuw.edu.pl/js/jquery-usos/css/tooltipster.css?hash=a3a7abd3e1f537d68d00759b283402733666da98'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/js/jquery-usos/css/tooltipster.4.0.css?hash=7031bdbed337b5dd535de3ff21ee16587adeef9e'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/css/jquery-usos/jquery-usos.css?hash=484387b2510f44f9e003a56049ad07feb6352d8e'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/css/theme/jquery-ui-1.10.1.custom.css?hash=072f68c9a7a80639c5a14acdc1ced5cba983f037'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/js/usos-ui/css/base.css?hash=a9237a7e22a7e1c72a260cae84ba7ce63c927598'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/js/jquery.fancybox/jquery.fancybox-1.3.4.css?hash=6dc674e0db76aaa75e3902bcd97ab936ae1a5eca'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/kontroler.php?_action=common/respacks/cssPack&module=akcje&hash=80a6f6009d24a7403c84b8f45eb2eca6'>
<link rel='stylesheet' href='https://usosweb.fuw.edu.pl/kontroler.php?_action=common/respacks/cssPack&module=akcje%2Fkatalog2%2Fprzedmioty&hash=178aebbc3a087df835760d808b811986'>

        <script src='https://usosweb.fuw.edu.pl/js/jquery-1.9.1.min.js?hash=05da65db36c2afbbb76c1baed7f52c5122064c77'></script>
<script src='https://usosweb.fuw.edu.pl/js/jquery-migrate-1.1.0.min.js?hash=5bed6cf694ecfe6ae0a4adb9bc58a1339cdcc629'></script>
<script src='https://usosweb.fuw.edu.pl/js/jquery-ui-1.10.1.custom.min.js?hash=8908365116b5257cc610946b79ee827d5b0c1b47'></script>
<script src='https://usosweb.fuw.edu.pl/js/jquery-usos/latest-bundle.min.js?hash=e1b5561800303de173d34f4b749c133bbae5d2cb'></script>
<script src='https://usosweb.fuw.edu.pl/js/common.js?hash=7f844a1881488a9243744712a378a78066c1c597'></script>
<script src='https://usosweb.fuw.edu.pl/js/vendor/URI-min.js?hash=b568becf245c9dabc64c7feef379b4d776b27820'></script>
<script src='https://usosweb.fuw.edu.pl/js/jquery.fancybox/jquery.fancybox-1.3.4.pack.js?hash=248552e90d8aa56044399de10a7c48144d2f4c2e'></script>
<script type='module' src='https://usosweb.fuw.edu.pl/js/usos-ui/index.js?hash=9b1301ed336fb31fafb8f767a0417ccda572fda7'></script>
<script src='https://usosweb.fuw.edu.pl/kontroler.php?_action=common/respacks/jsPack&module=akcje&hash=c1b0e40b3397fa97b2487e711929bd11'></script>
<script src='https://usosweb.fuw.edu.pl/kontroler.php?_action=common/respacks/jsPack&module=akcje%2Fkatalog2%2Fprzedmioty&hash=441266cba7804aadff523577f65aa6b3'></script>

    </head>
    <body >
                <skip-links menu-selector='menu-top' submenu-selector='menu-left' main-content-selector='#layout-main-content'></skip-links>
        <usos-layout >
                <div class='do_not_print'>
            <cas-bar id='layout-cas-bar' logged-user='Grzegorz Szymanek' mode='user'
                 logout-url='https://usosweb.fuw.edu.pl/kontroler.php?_action=logowaniecas/wyloguj' passwd-url='https://logowanie.uw.edu.pl/cas/../passwd-change/change?locale=pl'>
                <div slot='service-name'><b>Uniwersytet Warszawski</b> - Centralny System Uwierzytelniania</div>
            </cas-bar>
        </div>

        <div id='layout-container'>
            <div id='wrpopup'></div>

            
            
            <app-header
                display-name="Uniwersytet Warszawski, Wydział Fizyki"
                background-image-url="https://usosweb.fuw.edu.pl/kontroler.php?_action=common/getLocalStatic&file=header-image.png&mtime=1659616903"
                href="https://usosweb.fuw.edu.pl/kontroler.php?_action=news/default">
                <img slot="logo-img" src="https://usosweb.fuw.edu.pl//img/header-logo.svg" alt="Strona główna">
            </app-header>

            
    <menu-top tabindex="0">
        <menu-top-item href='https://usosweb.fuw.edu.pl/kontroler.php?_action=news/default' name='AKTUALNO&Sacute;CI' onclick='return Common.confirmWarnings();' ></menu-top-item> <menu-top-item href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/index' name='KATALOG' onclick='return Common.confirmWarnings();'  selected></menu-top-item> <menu-top-item href='https://usosweb.fuw.edu.pl/kontroler.php?_action=home/index' name='M&Oacute;J USOSWEB' onclick='return Common.confirmWarnings();' ></menu-top-item> <menu-top-item href='https://usosweb.fuw.edu.pl/kontroler.php?_action=dla_stud/index' name='DLA STUDENT&Oacute;W' onclick='return Common.confirmWarnings();' ></menu-top-item> <menu-top-item href='javascript:alert("Ta część serwisu jest dostępna tylko dla pracowników.")' name='DLA PRACOWNIKÓW'  greyed></menu-top-item> <menu-top-item href='https://usosweb.fuw.edu.pl/kontroler.php?_action=dodatki/index' name='DLA WSZYSTKICH' onclick='return Common.confirmWarnings();' ></menu-top-item> 
    </menu-top>


            <main-panel id="main">
                
<menu-left slot="left-menu" tabindex="0" aria-label="Panel boczny">
    <ul><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/index' onclick='return Common.confirmWarnings();'>NA SKRÓTY</a></li><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/osoby/index' onclick='return Common.confirmWarnings();'>STUDENCI, PRACOWNICY</a></li><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/index' onclick='return Common.confirmWarnings();'>JEDNOSTKI ORGANIZACYJNE</a></li><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/index' onclick='return Common.confirmWarnings();'>PRZEDMIOTY</a><ul><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=1100-2AF23' onclick='return Common.confirmWarnings();' class=' dynamic'>Mechanika kwantowa</a><ul><li><span class=' selected dynamic'>Semestr letni 2022/23 - Ćwiczenia (CW)</span><ul></ul></li></ul></li></ul></li><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/programy/index' onclick='return Common.confirmWarnings();'>STUDIA</a></li><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/akademiki/index' onclick='return Common.confirmWarnings();'>AKADEMIKI</a></li><li><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/pomoc' onclick='return Common.confirmWarnings();'>POMOC</a></li></ul>
    </menu-left>

                <main id="layout-main-content" slot="page-body" tabindex="0">
                                                                
<div id='layout-c22'>
            
    <div class='usos-ui'>

<div style='float:right'><a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/pomoc&section=przedmioty' onclick='return Common.confirmWarnings();'  tabindex='0'  ><span class='material-icons' style='color: var(--primary); font-size: 2rem;'>help</span></a></div>
<h1>
    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&kod=1100-2AF23' onclick='return Common.confirmWarnings();'  tabindex='0'  >Mechanika kwantowa</a>    <span class='note'>1100-2AF23</span>
    <br>
    Ćwiczenia (CW)
    <span class='note'>Semestr letni 2022/23</span>
</h1>

<usos-frame style='width: fit-content;'>
    <h2 slot='title'>Informacje o zajęciach (wspólne dla wszystkich grup)</h2>
    <div class='hide-borders'>
        <table class='grey'><tbody class='autostrong'>
                        <tr>
                <td class='strong'>Liczba godzin:</td>
                <td>
                    60
                </td>
            </tr>
            <tr>
                <td class='strong'>Limit miejsc:</td>
                <td>
                    80                </td>
            </tr>
                                                                                            </tbody></table>
    </div>
</usos-frame>

<h2>Grupy zajęciowe</h2>

<p>
    <usos-link icon-location='right' bordered>
        <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPlanZajecPrzedmiotu&prz_kod=1100-2AF23&cdyd_kod=2022L' onclick='return Common.confirmWarnings();'  tabindex='0'  >zobacz na planie zajęć</a>    </usos-link>
</p>

<table class='grey'>
    <tr>
        <th>Grupa</th>
        <th>Termin(y)</th>
        <th>Prowadzący</th>
        <th>
            Miejsca            <usos-tooltip style='font-size:15px;'  >Liczba osób w grupie / limit miejsc</usos-tooltip>        </th>
        <th class='strong'>Akcje</th>
            </tr>
            <tr >
            <td class='strong grupa' style='text-align:center'>1</td>
            <td>
                                                            każdy piątek, 10:15 - 12:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=4010' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala B0.17</a>                                                <br>
                                            każdy poniedziałek, 13:15 - 15:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3474' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 2.08</a>                                                <br>
                                                </td>
            <td>
                                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/osoby/pokazOsobe&os_id=3000' onclick='return Common.confirmWarnings();'  tabindex='0'  >Katarzyna Krajewska</a>                            </td>
            <td class="to-center">
                9/20
            </td>
            <td>
                <usos-link icon-location='right' inline>
                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=501608&gr_nr=1' onclick='return Common.confirmWarnings();'  tabindex='0'  >szczegóły</a>                </usos-link>
            </td>
                    </tr>
            <tr class='strong'>
            <td class='strong grupa' style='text-align:center'>2</td>
            <td>
                                                            każdy wtorek, 16:15 - 18:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=4011' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala B0.21</a>                                                <br>
                                            każdy czwartek, 16:15 - 18:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3478' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 2.24</a>                                                <br>
                                                </td>
            <td>
                                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/osoby/pokazOsobe&os_id=322362' onclick='return Common.confirmWarnings();'  tabindex='0'  >Mateusz Homenda</a>                            </td>
            <td class="to-center">
                17/24
            </td>
            <td>
                <usos-link icon-location='right' inline>
                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=501608&gr_nr=2' onclick='return Common.confirmWarnings();'  tabindex='0'  >szczegóły</a>                </usos-link>
            </td>
                    </tr>
            <tr >
            <td class='strong grupa' style='text-align:center'>3</td>
            <td>
                                                            każdy piątek, 12:15 - 14:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3469' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 1.38</a>                                                <br>
                                            każdy czwartek, 9:15 - 11:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3464' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 1.02</a>                                                <br>
                                                </td>
            <td>
                                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/osoby/pokazOsobe&os_id=3000' onclick='return Common.confirmWarnings();'  tabindex='0'  >Katarzyna Krajewska</a>                            </td>
            <td class="to-center">
                23/24
            </td>
            <td>
                <usos-link icon-location='right' inline>
                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=501608&gr_nr=3' onclick='return Common.confirmWarnings();'  tabindex='0'  >szczegóły</a>                </usos-link>
            </td>
                    </tr>
            <tr class='strong'>
            <td class='strong grupa' style='text-align:center'>4</td>
            <td>
                                                            każdy wtorek, 9:15 - 11:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3472' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 2.06</a>                                                <br>
                                            każdy czwartek, 9:15 - 11:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3469' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 1.38</a>                                                <br>
                                                </td>
            <td>
                                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/osoby/pokazOsobe&os_id=251824' onclick='return Common.confirmWarnings();'  tabindex='0'  >Krzysztof Myśliwy</a>                            </td>
            <td class="to-center">
                22/24
            </td>
            <td>
                <usos-link icon-location='right' inline>
                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=501608&gr_nr=4' onclick='return Common.confirmWarnings();'  tabindex='0'  >szczegóły</a>                </usos-link>
            </td>
                    </tr>
            <tr >
            <td class='strong grupa' style='text-align:center'>5</td>
            <td>
                                                            każdy czwartek, 15:15 - 17:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3464' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 1.02</a>                                                <br>
                                            każdy wtorek, 9:15 - 11:00,
                                                                            <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazSale&sala_id=3471' onclick='return Common.confirmWarnings();'  tabindex='0'  >sala 2.03</a>                                                <br>
                                                </td>
            <td>
                                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/osoby/pokazOsobe&os_id=309902' onclick='return Common.confirmWarnings();'  tabindex='0'  >Bartłomiej Bąk</a>                            </td>
            <td class="to-center">
                12/24
            </td>
            <td>
                <usos-link icon-location='right' inline>
                    <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=501608&gr_nr=5' onclick='return Common.confirmWarnings();'  tabindex='0'  >szczegóły</a>                </usos-link>
            </td>
                    </tr>
                <tfoot><tr class='footnote'>
            <td colspan="5">
                Wszystkie zajęcia odbywają się w budynku:<br>
                <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=katalog2/jednostki/pokazBudynek&bud_kod=3113' onclick='return Common.confirmWarnings();'  tabindex='0'  ><b>W.Fizyki budynek A i B  CeNT II  - Pasteura 5</b></a>            </td>
        </tr></tfoot>
    </table>


<div style='margin-top: 20px; color: #888; text-align: center'>
    Opisy przedmiotów w USOS i USOSweb są chronione prawem autorskim.<br> Właścicielem praw autorskich jest Uniwersytet Warszawski. </div>
</div>

<script type='text/javascript'>
    var LOCALS = {
        url: Common.actionLink("dodatki/moodle/ajax/kursyDoGrupZajec"),
        cykle: [{
            kodCykluDydaktycznego: '2022L',
            czyPokazywacKursyMoodle: '',
            parametry: {
                idZajecCyklu: '501608'
            }
        }]
    }
</script>
</div>

                                    </main>
            </main-panel>

            <usos-footer style="min-height: 4.75rem; font-size: 80%;">
                <div id="footer-logo">
                    <img src="https://usosweb.fuw.edu.pl/kontroler.php?_action=common/getLocalStatic&file=footer-logo.svg&mtime=1659616675" alt="USOS">

                </div>
                <footer-panel id="footer-university" header="Uniwersytet Warszawski, Wydział Fizyki">
                                                                                                        <footer-row icon="location"><span>ul. Ludwika Pasteura 5, 02-093 Warszawa</span></footer-row>
                                                                <footer-row icon="phone"><a href="tel:(+48)225532000">tel: (+48) 22 5532 000</a></footer-row>
                                                                <footer-row icon="www"><a href="https://www.fuw.edu.pl">https://www.fuw.edu.pl</a></footer-row>
                                    </footer-panel>
                <footer-panel id="footer-system" header="Uniwersytecki System Obsługi Studiów\nUSOSweb">
                    <footer-row icon="post-office">
                        <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=news/kontakt' onclick='return Common.confirmWarnings();'  tabindex='0'  >kontakt</a>                    </footer-row>
                    <footer-row icon="accessibility">
                        <a href='https://usosweb.fuw.edu.pl/kontroler.php?_action=news/deklaracjaDostepnosci' onclick='return Common.confirmWarnings();'  tabindex='0'  >deklaracja dostępności</a>                    </footer-row>
                    <footer-row icon="privacy-tip">
                        USOSweb 7.0.0.0 (2023-07-12)
                    </footer-row>

                </footer-panel>
            </usos-footer>
            <usos-copyright>
                <div slot="debug">
                    <p>
                                            </p>
                                                        </div>
            </usos-copyright>
        </div>

        
        
        </usos-layout>
        <top-scroller></top-scroller>
    </body>
</html>

'''