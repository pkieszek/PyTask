import json
import os
import re
from datetime import datetime
import logging
from colorama import Fore, Style, init

init(autoreset=True)

TASKS_FILE = "tasks.json"
LOG_FILE = "pytask.log"


class Task:
    """Klasa reprezentująca pojedyncze zadanie."""
    
    def __init__(self, task_id, title, priority="średni", done=False, created=None):
        self.id = task_id
        self.title = title
        self.priority = priority
        self.done = done
        self.created = created if created else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    def to_dict(self):
        """Konwertuje obiekt zadania do słownika."""
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "done": self.done,
            "created": self.created
        }
    
    @staticmethod
    def from_dict(data):
        """Tworzy obiekt Task ze słownika."""
        return Task(
            task_id=data["id"],
            title=data["title"],
            priority=data.get("priority", "średni"),
            done=data.get("done", False),
            created=data.get("created")
        )
    
    def mark_as_done(self):
        """Oznacza zadanie jako wykonane."""
        self.done = True
    
    def update(self, title=None, priority=None):
        """Aktualizuje dane zadania."""
        if title:
            self.title = title
        if priority and priority in ["niski", "średni", "wysoki"]:
            self.priority = priority
    
    def __str__(self):
        """Reprezentacja tekstowa zadania."""
        status = "✅" if self.done else "❌"
        return f"[{self.id}] {status} {self.title} ({self.priority}) - {self.created}"


class TaskManager:
    """Klasa zarządzająca listą zadań."""
    
    def __init__(self, filename=TASKS_FILE):
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Wczytuje listę zadań z pliku JSON."""
        if not os.path.exists(self.filename):
            self.tasks = []
            return
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(t) for t in data]
        except json.JSONDecodeError:
            print(Fore.RED + "❌ Błąd w pliku JSON. Tworzę nową listę zadań.")
            self.tasks = []
    
    def save_tasks(self):
        """Zapisuje listę zadań do pliku JSON."""
        with open(self.filename, "w", encoding="utf-8") as f:
            data = [task.to_dict() for task in self.tasks]
            json.dump(data, f, indent=4, ensure_ascii=False)
        log_action("Zapisano zadania")
    
    def add_task(self, title, priority="średni"):
        """Dodaje nowe zadanie do listy."""
        new_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(new_id, title, priority)
        self.tasks.append(task)
        return task
    
    def get_task_by_id(self, task_id):
        """Znajduje zadanie po ID."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def delete_task(self, task_id):
        """Usuwa zadanie z listy."""
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return task
        return None
    
    def get_filtered_tasks(self, done=None):
        """Zwraca przefiltrowaną listę zadań."""
        if done is None:
            return self.tasks
        return [t for t in self.tasks if t.done == done]
    
    def sort_by_priority(self):
        """Sortuje zadania po priorytecie."""
        prio_map = {"wysoki": 0, "średni": 1, "niski": 2}
        return sorted(self.tasks, key=lambda t: prio_map.get(t.priority, 3))
    
    def sort_by_date(self, reverse=True):
        """Sortuje zadania po dacie utworzenia."""
        return sorted(self.tasks, key=lambda t: t.created, reverse=reverse)
    
    def search_tasks(self, pattern):
        """Wyszukuje zadania używając wyrażeń regularnych."""
        regex = re.compile(pattern, re.IGNORECASE)
        return [t for t in self.tasks if regex.search(t.title)]


class Logger:
    """Klasa do logowania akcji."""
    
    def __init__(self, log_file=LOG_FILE):
        self.log_file = log_file
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s %(message)s"
        )
    
    def log(self, action, details=None):
        """Loguje akcję."""
        if details:
            logging.info(f"{action}: {details}")
        else:
            logging.info(action)


# Globalna instancja loggera
logger = Logger()

def log_action(action, task=None):
    """Kompatybilność wsteczna - używa klasy Logger."""
    logger.log(action, task)

def validate_priority(priority_input):
    """Waliduje priorytet używając wyrażeń regularnych."""
    # Wyrażenie regularne: dopasowuje "niski", "średni", "wysoki" (case-insensitive)
    pattern = r'^(niski|średni|wysoki)$'
    if re.match(pattern, priority_input, re.IGNORECASE):
        return priority_input.lower()
    return None


def validate_email_in_title(title):
    """
    Sprawdza czy w tytule zadania jest email (demonstracja regex).
    Zwraca listę znalezionych adresów email.
    """
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    return re.findall(email_pattern, title)


def add_task(task_manager):
    """Dodaje nowe zadanie do listy."""
    title = input(Fore.YELLOW + "📌 Podaj nazwę zadania: ").strip()
    if not title:
        print(Fore.RED + "⚠️ Nazwa nie może być pusta!")
        return
    
    # Sprawdzenie czy tytuł zawiera email (demonstracja regex)
    emails = validate_email_in_title(title)
    if emails:
        print(Fore.CYAN + f"ℹ️  Znaleziono adres(y) email w tytule: {', '.join(emails)}")
    
    priority_input = input(Fore.YELLOW + "Priorytet (niski/średni/wysoki): ").lower().strip()
    
    # Walidacja priorytetu używając regex
    priority = validate_priority(priority_input)
    if not priority:
        print(Fore.YELLOW + "⚠️ Niepoprawny priorytet, ustawiam 'średni'")
        priority = "średni"
    
    task = task_manager.add_task(title, priority)
    print(Fore.GREEN + "✅ Zadanie dodane!")
    log_action("Dodano zadanie", title)

def show_tasks(tasks, only_active=False):
    """Wyświetla listę zadań (przyjmuje listę obiektów Task)."""
    if only_active:
        filtered = [t for t in tasks if not t.done]
    else:
        filtered = tasks
    
    if not filtered:
        print(Fore.CYAN + "📭 Brak zadań do wyświetlenia.")
        return
    
    print(Fore.BLUE + "\n===== LISTA ZADAŃ =====")
    for t in filtered:
        status = Fore.GREEN + "✅" if t.done else Fore.RED + "❌"
        prio_color = {
            "wysoki": Fore.RED,
            "średni": Fore.YELLOW,
            "niski": Fore.GREEN
        }.get(t.priority, Fore.WHITE)
        print(f"{Style.BRIGHT}[{t.id}] {status} {t.title} {Style.RESET_ALL}({prio_color}{t.priority}{Style.RESET_ALL}) - utworzono {t.created}")
    print(Fore.BLUE + "========================\n")

def mark_done(task_manager):
    """Oznacza zadanie jako wykonane."""
    try:
        task_id = int(input(Fore.YELLOW + "Podaj ID zadania do oznaczenia jako wykonane: "))
    except ValueError:
        print(Fore.RED + "⚠️ Podaj poprawny numer ID!")
        return
    
    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(Fore.RED + "❌ Nie znaleziono zadania o tym ID.")
        return
    
    if task.done:
        print(Fore.CYAN + "To zadanie już jest wykonane.")
        return
    
    task.mark_as_done()
    print(Fore.GREEN + f"🟢 Zadanie '{task.title}' oznaczone jako wykonane.")
    log_action("Oznaczono jako wykonane", task.title)

def sort_and_filter(task_manager):
    """Sortuje i filtruje zadania według podanej opcji."""
    print(Fore.YELLOW + "Sortowanie/Filtracja:")
    print("1. Po priorytecie (wysoki->niski)")
    print("2. Po dacie utworzenia (najnowsze)")
    print("3. Tylko wykonane")
    print("4. Tylko niewykonane")
    print("5. Szukaj zadań (regex)")
    print("6. Anuluj")
    opt = input("Wybierz opcję (1-6): ").strip()
    
    if opt == "1":
        sorted_tasks = task_manager.sort_by_priority()
        show_tasks(sorted_tasks)
    elif opt == "2":
        sorted_tasks = task_manager.sort_by_date()
        show_tasks(sorted_tasks)
    elif opt == "3":
        show_tasks(task_manager.get_filtered_tasks(done=True))
    elif opt == "4":
        show_tasks(task_manager.get_filtered_tasks(done=False))
    elif opt == "5":
        search_tasks(task_manager)
    elif opt == "6":
        return
    else:
        print(Fore.RED + "Nieznana opcja.")


def search_tasks(task_manager):
    """Wyszukuje zadania używając wyrażeń regularnych."""
    print(Fore.CYAN + "\n🔍 Wyszukiwanie zadań (wyrażenia regularne)")
    print(Fore.WHITE + "UWAGA: Wpisuj bez cudzysłowów!\n")
    print("Przykłady wzorców:")
    print("  - zakupy       → znajdzie zadania zawierające słowo 'zakupy'")
    print("  - ^projekt     → zadania zaczynające się od 'projekt'")
    print("  - raport$      → zadania kończące się na 'raport'")
    print("  - task[0-9]+   → zadania zawierające 'task' i cyfry (np. task123)")
    print("  - email|telefon → zadania zawierające 'email' LUB 'telefon'\n")
    
    pattern = input(Fore.YELLOW + "Podaj wzorzec wyszukiwania (bez cudzysłowów): ").strip()
    
    # Usuń cudzysłowy jeśli użytkownik je wpisał
    pattern = pattern.strip("'\"")
    
    if not pattern:
        print(Fore.RED + "⚠️ Wzorzec nie może być pusty!")
        return
    
    try:
        results = task_manager.search_tasks(pattern)
        if results:
            print(Fore.GREEN + f"\n✅ Znaleziono {len(results)} zadań dla wzorca: '{pattern}'")
            show_tasks(results)
        else:
            print(Fore.CYAN + f"📭 Nie znaleziono zadań pasujących do wzorca: '{pattern}'")
            print(Fore.YELLOW + "Wskazówka: Wyszukiwanie nie uwzględnia wielkości liter.")
    except re.error as e:
        print(Fore.RED + f"❌ Niepoprawne wyrażenie regularne: {e}")

def delete_task(task_manager):
    """Usuwa zadanie z listy."""
    try:
        task_id = int(input(Fore.YELLOW + "Podaj ID zadania do usunięcia: "))
    except ValueError:
        print(Fore.RED + "⚠️ Podaj poprawny numer ID!")
        return
    
    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(Fore.RED + "❌ Nie znaleziono zadania o tym ID.")
        return
    
    confirm = input(Fore.RED + f"Czy na pewno chcesz usunąć '{task.title}'? (t/n): ").lower()
    if confirm == "t":
        removed = task_manager.delete_task(task_id)
        print(Fore.GREEN + f"🗑️ Zadanie '{removed.title}' usunięte.")
        log_action("Usunięto zadanie", removed.title)
    else:
        print(Fore.CYAN + "Anulowano usuwanie.")

def edit_task(task_manager):
    """Edytuje tytuł lub priorytet zadania."""
    try:
        task_id = int(input(Fore.YELLOW + "Podaj ID zadania do edycji: "))
    except ValueError:
        print(Fore.RED + "⚠️ Podaj poprawny numer ID!")
        return
    
    task = task_manager.get_task_by_id(task_id)
    if not task:
        print(Fore.RED + "❌ Nie znaleziono zadania o tym ID.")
        return
    
    print(f"Obecny tytuł: {task.title}")
    new_title = input("Nowy tytuł (Enter by zostawić): ").strip()
    
    print(f"Obecny priorytet: {task.priority}")
    new_priority_input = input("Nowy priorytet (niski/średni/wysoki, Enter by zostawić): ").lower().strip()
    
    # Walidacja priorytetu używając regex
    new_priority = None
    if new_priority_input:
        new_priority = validate_priority(new_priority_input)
        if not new_priority:
            print(Fore.YELLOW + "⚠️ Niepoprawny priorytet, pozostawiam obecny.")
    
    task.update(title=new_title if new_title else None, priority=new_priority)
    print(Fore.GREEN + "✏️ Zadanie zaktualizowane.")
    log_action("Edytowano zadanie", task.title)

def main_menu():
    """Główna pętla programu."""
    task_manager = TaskManager()
    
    while True:
        print(Fore.CYAN + Style.BRIGHT + "===== PyTask =====")
        print("1️⃣  Dodaj zadanie")
        print("2️⃣  Pokaż wszystkie zadania")
        print("3️⃣  Pokaż tylko aktywne")
        print("4️⃣  Oznacz jako wykonane")
        print("5️⃣  Sortuj/Filtruj/Szukaj zadania")
        print("6️⃣  Edytuj zadanie")
        print("7️⃣  Usuń zadanie")
        print("8️⃣  Zapisz i wyjdź")
        print("=================")
        choice = input(Fore.YELLOW + "Wybierz opcję (1-8): ").strip()

        if choice == "1":
            add_task(task_manager)
        elif choice == "2":
            show_tasks(task_manager.tasks)
        elif choice == "3":
            show_tasks(task_manager.tasks, only_active=True)
        elif choice == "4":
            mark_done(task_manager)
        elif choice == "5":
            sort_and_filter(task_manager)
        elif choice == "6":
            edit_task(task_manager)
        elif choice == "7":
            delete_task(task_manager)
        elif choice == "8":
            task_manager.save_tasks()
            print(Fore.GREEN + "💾 Zapisano zmiany. Do zobaczenia!")
            break
        else:
            print(Fore.RED + "⚠️ Nieznana opcja, spróbuj ponownie.")


if __name__ == "__main__":
    main_menu()