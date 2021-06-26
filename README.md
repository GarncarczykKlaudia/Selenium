# Test strony https://www.zalando.pl


- Informacje na temat testu:

    Środowisko: Chrome wersja 90.0.4430.212, Ubuntu 20.04 LTS

    Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

    Kroki:
    1. Wejdź na stronę "https://wizzair.com/pl-pl#/"
    2. Kliknij "ZALOGUJ SIĘ"
    3. Kliknij "REJESTRACJA"
    4. Wpisz imię
    5. Wpisz nazwisko
    6. Wybierz płeć
    7. Wprowadź nr telefonu
    8. Wprowadź niepoprawny e-mail
    9. Wprowadź hasło
    10. Wybierz kraj
    Oczekiwany rezultat:
    Rejestracja nie powodzi się
    Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny

- Uruchomienie testu

  $ python3 zalando.py
