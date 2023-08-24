# Lista z WIKI: https://pl.wikipedia.org/wiki/Uniwersytecki_System_Obs%C5%82ugi_Studi%C3%B3w
Unis = [
    # Udziałowcy MUCI:
    'Uniwersytet im. Adama Mickiewicza w Poznaniu',
    'Uniwersytet Jagielloński',
    'Uniwersytet Kardynała Stefana Wyszyńskiego',
    'Uniwersytet Kazimierza Wielkiego',
    'Uniwersytet Łódzki',
    'Uniwersytet Marii Curie-Skłodowskiej',
    'Uniwersytet Mikołaja Kopernika w Toruniu',
    'Uniwersytet Opolski',
    'Uniwersytet Śląski',
    'Uniwersytet w Białymstoku',
    'Uniwersytet Warmińsko-Mazurski',
    'Uniwersytet Warszawski',
    'Uniwersytet Wrocławski',
    # Członkowie Stowarzyszeni MUCI w ramach projektu USOS:,
    'Akademia Finansów i Biznesu Vistula',
    'Akademia Górniczo-Hutnicza im. Stanisława Staszica w Krakowie',
    'Akademia Ignatianum w Krakowie',
    'Akademia Kaliska im. Prezydenta Stanisława Wojciechowskiego',
    'Akademia Medycznych i Społecznych Nauk Stosowanych',
    'Akademia Muzyczna im. Feliksa Nowowiejskiego w Bydgoszczy',
    'Akademia Nauk Stosowanych Angelusa Silesiusa',
    'Akademia Nauk Stosowanych im. Stanisława Staszica w Pile',
    'Akademia Nauk Stosowanych Stefana Batorego',
    'Akademia Nauk Stosowanych w Elblągu',
    'Akademia Nauk Stosowanych w Koninie',
    'Akademia Nauk Stosowanych w Łomży',
    'Akademia Pedagogiki Specjalnej im. Marii Grzegorzewskiej',
    'Akademia Sztuk Pięknych w Katowicach',
    'Akademia Teatralna im. Aleksandra Zelwerowicza w Warszawie',
    'Akademia Techniczno-Humanistyczna w Bielsku-Białej',
    'Akademia Wychowania Fizycznego im. Bronisława Czecha w Krakowie',
    'Akademia Wychowania Fizycznego im. Eugeniusza Piaseckiego w Poznaniu',
    'Akademia Wychowania Fizycznego w Katowicach',
    'Akademia Wychowania Fizycznego we Wrocławiu',
    'Bielska Wyższa Szkoła im. Józefa Tyszkiewicza',
    'Chrześcijańska Akademia Teologiczna w Warszawie',
    'Dolnośląska Szkoła Wyższa we Wrocławiu',
    'Instytut Biologii Doświadczalnej im. Marcelego Nenckiego Polskiej Akademii Nauk',
    'Karpacka Państwowa Uczelnia w Krośnie',
    'Krajowa Szkoła Sądownictwa i Prokuratury',
    'Małopolska Uczelnia Państwowa im. rotmistrza Witolda Pileckiego w Oświęcimiu',
    'Niepubliczna Wyższa Szkoła Medyczna we Wrocławiu',
    'Olsztyńska Szkoła Wyższa im. Józefa Rusieckiego',
    'Państwowa Akademia Nauk Stosowanych w Chełmie',
    'Państwowa Wyższa Szkoła Techniczno-Ekonomiczna im. ks. Bronisława Markiewicza w Jarosławiu',
    'Państwowa Wyższa Szkoła Zawodowa im. Jana Amosa Komeńskiego w Lesznie',
    'Państwowa Wyższa Szkoła Zawodowa w Głogowie',
    'Politechnika Białostocka',
    'Politechnika Bydgoska im. Jana i Jędrzeja Śniadeckich',
    'Politechnika Częstochowska',
    'Politechnika Koszalińska',
    'Politechnika Opolska',
    'Politechnika Poznańska',
    'Politechnika Rzeszowska im. Ignacego Łukasiewicza',
    'Politechnika Śląska',
    'Politechnika Świętokrzyska',
    'Politechnika Warszawska',
    'Politechnika Wrocławska',
    'Szkoła Główna Gospodarstwa Wiejskiego w Warszawie',
    'Szkoła Główna Handlowa w Warszawie',
    'Szkoła Główna Służby Pożarniczej',
    'Szkoła Główna Turystyki i Hotelarstwa Vistula',
    'Szkoła Wyższa Wymiaru Sprawiedliwości',
    'Uczelnia Państwowa im. Jana Grodka w Sanoku',
    'Uczelnia Techniczno-Handlowa im. Heleny Chodkowskiej',
    'Uniwersytet Ekonomiczny w Katowicach',
    'Uniwersytet Ekonomiczny w Krakowie',
    'Uniwersytet Ekonomiczny w Poznaniu',
    'Uniwersytet Ekonomiczny we Wrocławiu',
    'Uniwersytet Humanistyczno-Przyrodniczy im. Jana Długosza w Częstochowie',
    'Uniwersytet Medyczny im. Piastów Śląskich we Wrocławiu',
    'Uniwersytet Medyczny w Lublinie',
    'Uniwersytet Morski w Gdyni',
    'Uniwersytet Muzyczny Fryderyka Chopina',
    'Uniwersytet Papieski Jana Pawła II w Krakowie',
    'Uniwersytet Przyrodniczo-Humanistyczny w Siedlcach',
    'Uniwersytet Przyrodniczy we Wrocławiu',
    'Uniwersytet Rolniczy im. Hugona Kołłątaja w Krakowie',
    'Wojskowa Akademia Techniczna im. Jarosława Dąbrowskiego',
    'Wrocławska Akademia Biznesu w Naukach Stosowanych',
    'Wyższa Szkoła Bezpieczeństwa',
    'Wyższa Szkoła Bezpieczeństwa Publicznego i Indywidualnego w Krakowie „Apeiron”',
    'Wyższa Szkoła Ekonomiczna w Białymstoku',
    'Wyższa Szkoła Gospodarki Euroregionalnej im. Alcide De Gasperi w Józefowie',
    'Wyższa Szkoła Kadr Menedżerskich',
    'Wyższa Szkoła Prawa',
    'Wyższa Szkoła Turystyki i Ekologii',
    'Zachodniopomorski Uniwersytet Technologiczny w Szczecinie',
]

# lista potencjalnych adresów URL
przedrostki = [
    'usosapps.',
    'usosapps.uni.',
    'apps.',
    'apps.usos.',
    'api.',
    'api.usos.',
]
import requests
from bs4 import BeautifulSoup

linki_usos_api = []
# lookup every uni name in Unis list + 'USOS API' in google collect first 10 links and display -> let user choose the best one
# if user chooses one -> add it to linki_usos_api list
for uni in Unis:
    print(f'Looking for {uni} USOS API')
    query = f'{uni} USOS API'
    url = f"https://www.google.com/search?q={query}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    links = []
    for a in soup.find_all("a"):
        print(a)
        href = a.get("href")
        if href.startswith("/url?q="):
            link = href.split("/url?q=")[1].split("&")[0]
            links.append(link)
            if len(links) == 10:
                break
    print(links)
    link = None
    for url in links:
        print(url)
        # find the first one that contains one of the prefixes
        for prefix in przedrostki:
            if prefix in url:
                print(url)
                link = url
                break
        if link:
            break
    linki_usos_api.append(link)
    print('=============================')

# 