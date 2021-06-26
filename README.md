# Test strony https://www.zalando.pl


- Informacje na temat testu:

    Środowisko: Chrome wersja 90.0.4430.212, Ubuntu 20.04 LTS

    Warunek wstępny: Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

    Kroki:
  1. Wejdź na stronę "https://www.zalando.pl"
  2. Najedź na ikonę człowieka
  3. Kliknij "Jesteś nowym klientem"
  4. Zaakceptuj proponowane personalizacje
  5. Wpisz imię
  6. Wpisz e-mail
  7. Wprowadź hasło
  8. Kliknij zarejestruj
  Oczekiwany rezultat:
  Rejestracja nie powodzi się
  Użytkownik dostaje informację, że wypełnienie pola z nazwiskiem jest wymagane.

- Uruchomienie testu

  $ python3 zalando.py
