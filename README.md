# 📋 PyTask - Menedżer Zadań w Pythonie

Zaawansowany menedżer zadań z interfejsem konsolowym, wykorzystujący programowanie obiektowe, wyrażenia regularne i przechowywanie danych w formacie JSON.

## 📖 Opis Projektu

PyTask to aplikacja konsolowa do zarządzania listą zadań (to-do list), stworzona w Pythonie. Projekt demonstruje zaawansowane umiejętności programowania, w tym:

- ✅ Programowanie obiektowe (OOP) z trzema klasami
- ✅ Operacje na plikach JSON
- ✅ Wyrażenia regularne (regex)
- ✅ Kolorowy interfejs użytkownika (colorama)
- ✅ System logowania akcji
- ✅ Zaawansowane sortowanie i filtrowanie

## 🚀 Instalacja

### Wymagania
- Python 3.7 lub nowszy
- Biblioteka `colorama`

### Instalacja zależności

```bash
pip install colorama
```

### Uruchomienie

```bash
python main.py
```

## 🏗️ Architektura Projektu

### Klasy (Programowanie Obiektowe)

#### 1. `Task` - Reprezentacja zadania
Klasa reprezentująca pojedyncze zadanie z metodami:

```python
class Task:
    def __init__(self, task_id, title, priority="średni", done=False, created=None)
    def to_dict(self)              # Konwersja do słownika (JSON)
    def from_dict(data)            # Tworzenie z słownika (JSON)
    def mark_as_done(self)         # Oznaczanie jako wykonane
    def update(self, title, priority)  # Aktualizacja danych
```

**Atrybuty:**
- `id` - unikalny identyfikator zadania
- `title` - nazwa zadania
- `priority` - priorytet (niski/średni/wysoki)
- `done` - status wykonania (True/False)
- `created` - data i czas utworzenia

#### 2. `TaskManager` - Zarządzanie zadaniami
Klasa zarządzająca kolekcją zadań:

```python
class TaskManager:
    def load_tasks(self)           # Wczytywanie z JSON
    def save_tasks(self)           # Zapisywanie do JSON
    def add_task(self, title, priority)
    def get_task_by_id(self, task_id)
    def delete_task(self, task_id)
    def get_filtered_tasks(self, done)
    def sort_by_priority(self)
    def sort_by_date(self, reverse)
    def search_tasks(self, pattern)  # Wyszukiwanie z regex
```

**Odpowiedzialności:**
- Przechowywanie listy zadań w pamięci
- Operacje CRUD (Create, Read, Update, Delete)
- Serializacja/deserializacja JSON
- Sortowanie i filtrowanie

#### 3. `Logger` - System logowania
Klasa odpowiedzialna za zapisywanie historii akcji:

```python
class Logger:
    def __init__(self, log_file)
    def log(self, action, details)
```

**Funkcje:**
- Zapisuje wszystkie akcje do pliku `pytask.log`
- Format: `YYYY-MM-DD HH:MM:SS Akcja: szczegóły`

## 🎯 Funkcjonalności

### 1️⃣ Dodawanie zadań
- Podajesz nazwę zadania
- Wybierasz priorytet (niski/średni/wysoki)
- **Regex:** Automatyczne wykrywanie adresów email w tytule
- **Regex:** Walidacja priorytetu wyrażeniem regularnym

### 2️⃣ Wyświetlanie zadań
- Wszystkie zadania z kolorowym statusem
- Tylko aktywne (niewykonane)
- Kolorowe priorytety: czerwony (wysoki), żółty (średni), zielony (niski)

### 3️⃣ Oznaczanie jako wykonane
- Zmiana statusu zadania na "wykonane"
- Zapisywane w historii (log)

### 4️⃣ Sortowanie/Filtracja
- **Po priorytecie:** wysoki → średni → niski
- **Po dacie:** najnowsze pierwsze
- **Filtr:** tylko wykonane
- **Filtr:** tylko niewykonane

### 5️⃣ Wyszukiwanie z Regex 🔍
Zaawansowane wyszukiwanie używając wyrażeń regularnych:

**Przykłady wzorców:**
- `zakupy` - znajdzie wszystkie zadania zawierające "zakupy"
- `^projekt` - zadania zaczynające się od "projekt"
- `raport$` - zadania kończące się na "raport"
- `task[0-9]+` - zadania zawierające "task" i cyfry (np. task123)
- `email|telefon` - zadania zawierające "email" LUB "telefon"

### 6️⃣ Edycja zadań
- Zmiana tytułu
- Zmiana priorytetu
- **Regex:** Walidacja nowego priorytetu

### 7️⃣ Usuwanie zadań
- Usuwanie z potwierdzeniem
- Zapisane w historii

### 8️⃣ Automatyczny zapis
- Wszystkie zmiany zapisywane do `tasks.json`
- Format JSON z wcięciami dla czytelności

## 📁 Struktura Plików

```
PyTask/
├── main.py          # Główny plik programu
├── tasks.json       # Baza danych zadań (JSON)
├── pytask.log       # Historia akcji
└── README.md        # Ten plik
```

## 🔧 Użyte Technologie i Koncepcje

### 1. Typy i Struktury Danych
- **Listy:** przechowywanie kolekcji zadań
- **Słowniki:** reprezentacja zadań w JSON
- **String, int, bool:** podstawowe typy danych
- **datetime:** znaczniki czasu

### 2. Programowanie Obiektowe (OOP)
- **3 klasy:** Task, TaskManager, Logger
- **Enkapsulacja:** dane i metody w jednej klasie
- **Metody statyczne:** `Task.from_dict()`
- **Metody instancji:** wszystkie metody klas

### 3. Wyrażenia Regularne (Regex)
```python
# 1. Walidacja priorytetu
pattern = r'^(niski|średni|wysoki)$'
re.match(pattern, priority_input, re.IGNORECASE)

# 2. Wykrywanie emaili
email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
re.findall(email_pattern, title)

# 3. Wyszukiwanie zadań
regex = re.compile(pattern, re.IGNORECASE)
regex.search(task.title)
```

### 4. Operacje JSON
```python
# Wczytywanie
with open(TASKS_FILE, "r", encoding="utf-8") as f:
    data = json.load(f)
    tasks = [Task.from_dict(t) for t in data]

# Zapisywanie
with open(TASKS_FILE, "w", encoding="utf-8") as f:
    data = [task.to_dict() for task in tasks]
    json.dump(data, f, indent=4, ensure_ascii=False)
```

### 5. Operacje Wejścia/Wyjścia
- `input()` - pobieranie danych od użytkownika
- `print()` - wyświetlanie informacji
- Operacje na plikach: `open()`, `read()`, `write()`
- Obsługa błędów: `try/except`

### 6. Dekompozycja Problemu
Program podzielony na funkcje:
- `add_task()` - dodawanie
- `show_tasks()` - wyświetlanie
- `mark_done()` - oznaczanie
- `sort_and_filter()` - sortowanie
- `search_tasks()` - wyszukiwanie
- `delete_task()` - usuwanie
- `edit_task()` - edycja
- `main_menu()` - główna pętla

## 📊 Przykład Pliku JSON

```json
[
    {
        "id": 1,
        "title": "Zrobić zakupy",
        "priority": "wysoki",
        "done": false,
        "created": "2024-11-18 14:30:00"
    },
    {
        "id": 2,
        "title": "Napisać raport",
        "priority": "średni",
        "done": true,
        "created": "2024-11-18 15:45:00"
    }
]
```

## 📝 Przykład Użycia

```
===== PyTask =====
1️⃣  Dodaj zadanie
2️⃣  Pokaż wszystkie zadania
3️⃣  Pokaż tylko aktywne
4️⃣  Oznacz jako wykonane
5️⃣  Sortuj/Filtruj/Szukaj zadania
6️⃣  Edytuj zadanie
7️⃣  Usuń zadanie
8️⃣  Zapisz i wyjdź
=================
Wybierz opcję (1-8): 1

📌 Podaj nazwę zadania: Spotkanie z klientem client@example.com
ℹ️  Znaleziono adres(y) email w tytule: client@example.com
Priorytet (niski/średni/wysoki): wysoki
✅ Zadanie dodane!

Wybierz opcję (1-8): 5

Sortowanie/Filtracja:
1. Po priorytecie (wysoki->niski)
2. Po dacie utworzenia (najnowsze)
3. Tylko wykonane
4. Tylko niewykonane
5. Szukaj zadań (regex)
6. Anuluj
Wybierz opcję (1-6): 5

🔍 Wyszukiwanie zadań (wyrażenia regularne)
Przykłady:
  - 'zakupy' - znajdzie zadania zawierające słowo 'zakupy'
  - '^projekt' - zadania zaczynające się od 'projekt'
  - 'raport$' - zadania kończące się na 'raport'
  - 'task[0-9]+' - zadania zawierające 'task' i cyfry
Podaj wzorzec wyszukiwania: @

✅ Znaleziono 1 zadań:

===== LISTA ZADAŃ =====
[1] ❌ Spotkanie z klientem client@example.com (wysoki) - utworzono 2024-11-18 14:30:00
========================
```

## 🎓 Wymagania Projektu

Ten projekt spełnia wszystkie wymagania zaliczenia przedmiotu:

- ✅ **Znajomość typów i struktur danych** - listy, słowniki, string, int, bool
- ✅ **Operacje wejścia/wyjścia** - input(), print(), operacje na plikach
- ✅ **Dekompozycja problemu** - podział na funkcje i klasy
- ✅ **Programowanie strukturalne** - funkcje z czystym kodem
- ✅ **Programowanie obiektowe** - 3 klasy z metodami i atrybutami
- ✅ **Format JSON** - wczytywanie i zapisywanie danych
- ✅ **Wyrażenia regularne** - 3 zastosowania regex

## 🐛 Obsługa Błędów

Program obsługuje:
- Niepoprawny format pliku JSON
- Brak pliku JSON (tworzy nowy)
- Niepoprawne ID zadania
- Niepoprawne wyrażenia regularne
- Puste dane wejściowe

## 📄 Licencja

Projekt edukacyjny - wolne użycie.

## 👨‍💻 Autor

Projekt stworzony jako zaliczenie przedmiotu z programowania w Pythonie.

## 🔮 Możliwe Rozszerzenia

- [ ] Kategorie zadań
- [ ] Daty deadline
- [ ] Eksport do CSV/PDF
- [ ] Interfejs graficzny (GUI)
- [ ] Synchronizacja z chmurą
- [ ] Przypomnienia
- [ ] Statystyki produktywności
