# PyTask 📝

**Prosty menedżer zadań w Pythonie, który stworzyłem.**

## Opis projektu
PyTask to lekki i intuicyjny menedżer zadań napisany przeze mnie w Pythonie, który umożliwia zarządzanie codziennymi zadaniami w terminalu. Projekt został rozszerzony o funkcje takie jak kolorowanie terminala dla lepszej czytelności statusów i priorytetów, logowanie działań użytkownika do pliku logów, sortowanie i filtrowanie zadań według różnych kryteriów, a także możliwość edycji i usuwania zadań.

## Wymagania
- Python 3.6 lub nowszy

## Instalacja zależności
Zamiast instalować biblioteki pojedynczo, przygotowałem plik `requirements.txt`, który zawiera wszystkie potrzebne pakiety. Aby zainstalować wymagane zależności, wystarczy wykonać:
```bash
pip install -r requirements.txt
```

## Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-repo/PyTask.git
   cd PyTask
   ```
2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install -r requirements.txt
   ```

## Uruchomienie
Aby uruchomić menedżer zadań, wystarczy, że wywołasz skrypt `main.py`:
```bash
python3 main.py
```

## Funkcjonalności
- Dodaję nowe zadania z przypisanym priorytetem.
- Oznaczam zadania jako wykonane.
- Wyświetlam listę wszystkich zadań lub tylko aktywnych.
- Sortuję zadania według priorytetu lub daty dodania.
- Filtruję zadania według statusu lub priorytetu.
- Edytuję istniejące zadania (zmieniam opis, priorytet).
- Usuwam zadania.
- Zapisuję i odczytuję dane z pliku JSON.
- Koloruję terminal dla lepszej czytelności statusów i priorytetów.
- Loguję działania użytkownika do pliku logów.
- Cofam ostatnią operację (undo).
- Wyszukuję zadania po słowie kluczowym w opisie.
- Usuwam wszystkie zadania oznaczone jako wykonane.
- Resetuję listę zadań (usuwam wszystkie).
- Eksportuję listę zadań do pliku CSV.

## Menu i opcje
Po uruchomieniu programu masz do dyspozycji następujące opcje (zgodnie z menu w programie):

1. **Dodaj zadanie** – dodaj nowe zadanie, podając opis i priorytet.
2. **Pokaż wszystkie zadania** – wyświetl całą listę zadań.
3. **Pokaż tylko aktywne** – wyświetl tylko zadania, które nie zostały oznaczone jako wykonane.
4. **Oznacz jako wykonane** – wybierz zadanie do oznaczenia jako wykonane.
5. **Sortuj/Filtruj zadania** – sortuj lub filtruj zadania według wybranych kryteriów (np. priorytet, status).
6. **Edytuj zadanie** – zmień opis lub priorytet wybranego zadania.
7. **Usuń zadanie** – usuń wybrane zadanie z listy.
8. **Zapisz i wyjdź** – zapisz wszystkie zmiany i zakończ działanie programu.

## Przykład działania
```
Witaj w PyTask!
1. Dodaj zadanie
2. Wyświetl zadania
3. Edytuj zadanie
4. Oznacz zadanie jako wykonane
5. Usuń zadanie
6. Wyszukaj zadania
7. Cofnij ostatnią operację
8. Usuń wszystkie wykonane zadania
9. Zresetuj listę zadań
10. Eksportuj zadania do CSV
11. Zapisz zmiany
12. Wyjdź
Wybierz opcję: 1

Podaj opis zadania: Zrobić zakupy
Podaj priorytet (niski, średni, wysoki): wysoki
Zadanie dodane pomyślnie!

Wybierz opcję: 2

Lista zadań:
[1] Zrobić zakupy - Priorytet: WYSOKI - Status: Aktywne

Wybierz opcję: 4
Podaj numer zadania do oznaczenia jako wykonane: 1
Zadanie oznaczone jako wykonane.

Wybierz opcję: 12
Do zobaczenia!
```

## Logi
Wszystkie działania użytkownika są zapisywane w pliku logów `logs/pytask.log`, co pozwala na śledzenie historii operacji i diagnozowanie ewentualnych problemów.

## Struktura plików
```
PyTask/
├── main.py           # Główny skrypt uruchamiający program
├── tasks.json        # Plik z zapisanymi zadaniami (generowany automatycznie)
├── requirements.txt  # Plik z listą wymaganych bibliotek
├── README.md         # Dokumentacja projektu
└── logs/
    └── pytask.log    # Plik logów działania programu
```

## Dalsze rozwinięcia
- Planuję integrację z kalendarzem Google lub innymi API do synchronizacji zadań.
- Chcę dodać powiadomienia i przypomnienia.
- Myślę o stworzeniu interfejsu graficznego (GUI) do wygodniejszego zarządzania zadaniami.
- Rozważam obsługę wielu użytkowników i zadań współdzielonych.
- Zamierzam wprowadzić eksport i import zadań w innych formatach (CSV, XML).

---

Dziękuję za korzystanie z PyTask! Jeśli masz sugestie lub chcesz zgłosić błąd, zapraszam do kontaktu lub utworzenia zgłoszenia na GitHub.
