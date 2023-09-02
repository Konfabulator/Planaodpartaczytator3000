
# Planaodpartaczytator3000

Odpartaczy każdy plan <span style="color:green;">niemal dowolnej, polskiej</span> uczelni zwracając wszystkie możliwe opcje we jednym schludnym pliku tekstowym.
<!-- write with italic -->
<span style="color:red;font-style:italic;">
    !!! Już teraz !!!<br>
    (Trochę nieprzetestowana) opcja wyboru uczelni obsługującej USOS!!!<br>
    Dodatkowo - prawie działająca opcja wyboru języka (PL/EN)!!!<br>
    To nie wszystko - można wybierać semestr podczas wprowadzania przedmiotu!!!
</span>

## <span style="color:orange;"> Obsługi Instrukcja </span>
Celem skorzystania z aplikacji wystarczy uruchomić plik "planaodpartaczytator3000.py".
(Brakujące biblioteki pythona [>=3.6] należy samodzielnie doinstalować).

- <span style="color:orange;">Podać nazwę pliku ze wszystkimi grupami zajęciowymi. </span>

    Zawartość pliku jest w formie:\
    <span style="color:violet;">
    "Nazwa Przedmiotu"\
    D h:mm - h:mm, D h:mm - h:mm, ...\
    D h:mm - h:mm, D h:mm - h:mm, ...\
    ... 
    </span>

    Gdzie D - to dzień tygodnia 1-5. Godziny zajęć
    jednej grupy rozdzielamy przecinkiem (", "), 
    a kolejne wiersze to grupy zajęciowe.

    
- <span style="color:orange;"> Podać czy plik ma zostać tylko przeanalizowany R, czy utworzony a następnie przeanalizowany W. </span>

    - Jeśli W - Użytkownik zostanie poproszony o wprowadzenie <span style="color:green;">KODU</span> Przedmiotu 
(<span style="color:red;">UWAGA: nie działa na żadne zajęcia ogólnouniwersyteckie - 
    należy je ręcznie wprowadzić do pliku</span>).
    Następnie zostaną utworzone wszystkie plany według R.

    - Jeśli R - Program rozpatrzy wszystkie kombinacje wszystkich wymienionych w pliku zajęć
    (z każdych zajęć zostanie wybrana jedna grupa)
    i poda tylko te bez "nakładek" w pliku: "Plany_{name}.txt" w formie eleganckich tabelek.

- <span style="color:orange;">To tyle. Życzę dobrej zabawy i miłego dnia</span>

## <span style="color:orange;"> Następne Wersje </span>
    Z nadzieją można wypatrywać przyszłych wersji, zawierających między innymi interfejs graficzny oraz wyszukiwarkę przedmiotów.

## Lista symboli obsługiwanych uczelni:
<span style="color:orange;">
<br>"AMISNS" :                                                                              "amisns"
<br>"Akademia Nauk Stosowanych Stefana Batorego" :                                          "ansb"
<br>"Akademia Wychowania Fizycznego im. Bronisława Czecha w Krakowie" :                     "awf"
<br>"Chrześcijańska Akademia Teologiczna" :                                                 "chat"
<br>"Jan Dlugosz University in Czestochowa" :                                               "ujd"
<br>"National Academy of Dramatic Art in Warsaw" :                                          "at"
<br>"PWSTE w Jarosławiu" :                                                                  "pwste"
<br>"SGH Warsaw School of Economics" :                                                      "sgh"
<br>"The Academy of Fine Arts and Design in Katowice" :                                     "asp"
<br>"The Adam Mickiewicz University in Poznan" :                                            "amu"
<br>"The Bialystok School of Economics" :                                                   "wse"
<br>"The Bydgoszcz University of Science and Technology" :                                  "pbs"
<br>"The Cardinal Stefan Wyszynski University" :                                            "uksw"
<br>"The Cracow University of Economic" :                                                   "uek"
<br>"The DSW University of Lower Silesia" :                                                 "dsw"
<br>"The Feliks Nowowiejski Academy of Music" :                                             "amuz"
<br>"The Helena Chodkowska University of Law in Wrocław" :                                  "prawowroclaw"
<br>"The Jagiellonian University" :                                                         "uj"
<br>"The Jerzy Kukuczka Academy of Physical Education in Katowice" :                        "awf"
<br>"The Kazimierz Wielki University" :                                                     "ukw"
<br>"The Kielce University of Technology" :                                                 "tuk"
<br>"The Krosno Academy of Applied Sciences" :                                              "kpu"
<br>"The Military University of Technology in Warsaw" :                                     "wat"
<br>"The Nicolaus Copernicus University" :                                                  "umk"
<br>"The Opole University of Technology" :                                                  "po"
<br>"The Pontifical University of John Paul II" :                                           "upjp2"
<br>"The Poznan University of Technology" :                                                 "put"
<br>"The Poznań University of Economics and Business" :                                     "uep"
<br>"The Rzeszów University of Technology" :                                                "prz"
<br>"The Siedlce University of Natural Sciences and Humanities" :                           "uph"
<br>"The Silesian University of Technology" :                                               "polsl"
<br>"The Stanisław Staszic State University of Applied Sciences in Piła" :                  "ans"
<br>"The Technical University of Koszalin" :                                                "tu"
<br>"The University University of Technology and Economics" :                               "uth"
<br>"The University of APS" :                                                               "aps"
<br>"The University of Agriculture" :                                                       "ur"
<br>"The University of Bialystok" :                                                         "uwb"
<br>"The University of Euroregional Economy in Józefów - Warsaw" :                          "wsge"
<br>"The University of Lodz" :                                                              "ul"
<br>"The University of Maria Curie-Skłodowska" :                                            "umcs"
<br>"The University of Opole" :                                                             "uop"
<br>"The University of Silesia in Katowice" :                                               "us"
<br>"The University of Warmia and Mazury in Olsztyn" :                                      "uwm"
<br>"The University of Warsaw" :                                                            "uw"
<br>"The University of Wroclaw" :                                                           "uwr"
<br>"The Warsaw University of Technology" :                                                 "pw"
<br>"The Wroclaw University of Economics" :                                                 "uew"
<br>"The Wroclaw University of Science and Technology" :                                    "pwr"
<br>"The Wrocław University of Environmental and Life Science" :                            "upwr"
<br>"The president Stanisław Wojciechowski Higher Vocational State School in Kalisz" :      "pwsz"
<br>"University of Lomza" :                                                                 "pwsip"
<br>"Uniwerstytet Muzyczny Fryderyka Chopina" :                                             "chopin"
<br>"VISTULA UNIVERSITY" :                                                                  "vistula"
<br>"Wyższa Szkoła Bezpieczeństwa Publicznego i Indywidualnego „Apeiron” w Krakowie" :      "apeiron"         
<br></span>
## Autor

- [@Konfabulator](https://github.com/Konfabulator)

