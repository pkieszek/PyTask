# PyTask 📝

**Prosty menedżer zadań w Pythonie, który stworzyłem.**

## Opis projektu
PyTask to lekki i intuicyjny menedżer zadań napisany przeze mnie w Pythonie, który umożliwia zarządzanie codziennymi zadaniami w terminalu. Rozszerzyłem projekt o funkcje takie jak kolorowanie terminala dla lepszej czytelności, logowanie działań użytkownika, sortowanie i filtrowanie zadań, a także możliwość edycji i usuwania zadań.

## Wymagania
- Python 3.6 lub nowszy
- Biblioteki Python:
  - `colorama` (do kolorowania terminala)
  - `logging` (wbudowany moduł Pythona)
  
## Instalacja
1. Sklonuj repozytorium:
   ```bash
   git clone https://github.com/twoje-repo/PyTask.git
   cd PyTask
   ```
2. Zainstaluj wymagane biblioteki:
   ```bash
   pip install colorama
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

## Menu i opcje
Po uruchomieniu programu masz do dyspozycji następujące opcje:
- **1. Dodaj zadanie** – wprowadź opis i priorytet nowego zadania.
- **2. Wyświetl zadania** – pokaż wszystkie lub tylko aktywne zadania, z opcją sortowania i filtrowania.
- **3. Oznacz zadanie jako wykonane** – wybierz zadanie do oznaczenia jako zakończone.
- **4. Edytuj zadanie** – zmodyfikuj opis lub priorytet istniejącego zadania.
- **5. Usuń zadanie** – usuń wybrane zadanie z listy.
- **6. Zapisz zmiany** – zapisz aktualny stan zadań do pliku JSON.
- **7. Wyjdź** – zakończ działanie programu.

## Przykład działania
```
Witaj w PyTask!
1. Dodaj zadanie
2. Wyświetl zadania
3. Oznacz zadanie jako wykonane
4. Edytuj zadanie
5. Usuń zadanie
6. Zapisz zmiany
7. Wyjdź
Wybierz opcję: 1

Podaj opis zadania: Zrobić zakupy
Podaj priorytet (niski, średni, wysoki): wysoki
Zadanie dodane pomyślnie!

Wybierz opcję: 2

Lista zadań:
[1] Zrobić zakupy - Priorytet: WYSOKI - Status: Aktywne

Wybierz opcję: 3
Podaj numer zadania do oznaczenia jako wykonane: 1
Zadanie oznaczone jako wykonane.

Wybierz opcję: 7
Do zobaczenia!
```

## Struktura plików
```
PyTask/
├── main.py           # Główny skrypt uruchamiający program
├── tasks.json        # Plik z zapisanymi zadaniami (generowany automatycznie)
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
