
# Planaodpartaczytator3000

Odpartaczy każdy plan uczelni <span style="color:green;">UW</span> zwracając wszystkie możliwe opcje we jednym schludnym pliku tekstowym.
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

## Autor

- [@Konfabulator](https://github.com/Konfabulator)

