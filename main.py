import json
import os
from datetime import datetime
import logging
from colorama import Fore, Style, init

init(autoreset=True)

TASKS_FILE = "tasks.json"
LOG_FILE = "pytask.log"

def log_action(action, task=None):
    logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s %(message)s")
    if task:
        logging.info(f"{action}: {task}")
    else:
        logging.info(action)

def load_tasks():
    """Wczytuje listę zadań z pliku JSON, jeśli istnieje."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(Fore.RED + "❌ Błąd w pliku JSON. Tworzę nową listę zadań.")
        return []

def save_tasks(tasks):
    """Zapisuje listę zadań do pliku JSON."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)
    log_action("Zapisano zadania")

def add_task(tasks):
    """Dodaje nowe zadanie do listy."""
    title = input(Fore.YELLOW + "📌 Podaj nazwę zadania: ").strip()
    if not title:
        print(Fore.RED + "⚠️ Nazwa nie może być pusta!")
        return
    priority = input(Fore.YELLOW + "Priorytet (niski/średni/wysoki): ").lower().strip()
    if priority not in ["niski", "średni", "wysoki"]:
        priority = "średni"
    new_task = {
        "id": max([t["id"] for t in tasks], default=0) + 1,
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    print(Fore.GREEN + "✅ Zadanie dodane!")
    log_action("Dodano zadanie", title)

def show_tasks(tasks, only_active=False):
    """Wyświetla listę zadań."""
    filtered = [t for t in tasks if not t["done"]] if only_active else tasks
    if not filtered:
        print(Fore.CYAN + "📭 Brak zadań do wyświetlenia.")
        return
    print(Fore.BLUE + "\n===== LISTA ZADAŃ =====")
    for t in filtered:
        status = Fore.GREEN + "✅" if t["done"] else Fore.RED + "❌"
        prio_color = {
            "wysoki": Fore.RED,
            "średni": Fore.YELLOW,
            "niski": Fore.GREEN
        }.get(t["priority"], Fore.WHITE)
        print(f"{Style.BRIGHT}[{t['id']}] {status} {t['title']} {Style.RESET_ALL}({prio_color}{t['priority']}{Style.RESET_ALL}) - utworzono {t['created']}")
    print(Fore.BLUE + "========================\n")

def mark_done(tasks):
    """Oznacza zadanie jako wykonane."""
    try:
        task_id = int(input(Fore.YELLOW + "Podaj ID zadania do oznaczenia jako wykonane: "))
    except ValueError:
        print(Fore.RED + "⚠️ Podaj poprawny numer ID!")
        return
    for t in tasks:
        if t["id"] == task_id:
            if t["done"]:
                print(Fore.CYAN + "To zadanie już jest wykonane.")
                return
            t["done"] = True
            print(Fore.GREEN + f"🟢 Zadanie '{t['title']}' oznaczone jako wykonane.")
            log_action("Oznaczono jako wykonane", t["title"])
            return
    print(Fore.RED + "❌ Nie znaleziono zadania o tym ID.")

def sort_and_filter(tasks):
    """Sortuje i filtruje zadania według podanej opcji."""
    print(Fore.YELLOW + "Sortowanie/Filtracja:")
    print("1. Po priorytecie (wysoki->niski)")
    print("2. Po dacie utworzenia (najnowsze)")
    print("3. Tylko wykonane")
    print("4. Tylko niewykonane")
    print("5. Anuluj")
    opt = input("Wybierz opcję (1-5): ").strip()
    if opt == "1":
        prio_map = {"wysoki": 0, "średni": 1, "niski": 2}
        sorted_tasks = sorted(tasks, key=lambda t: prio_map.get(t["priority"], 3))
        show_tasks(sorted_tasks)
    elif opt == "2":
        sorted_tasks = sorted(tasks, key=lambda t: t["created"], reverse=True)
        show_tasks(sorted_tasks)
    elif opt == "3":
        show_tasks([t for t in tasks if t["done"]])
    elif opt == "4":
        show_tasks([t for t in tasks if not t["done"]])
    elif opt == "5":
        return
    else:
        print(Fore.RED + "Nieznana opcja.")

def delete_task(tasks):
    """Usuwa zadanie z listy."""
    try:
        task_id = int(input(Fore.YELLOW + "Podaj ID zadania do usunięcia: "))
    except ValueError:
        print(Fore.RED + "⚠️ Podaj poprawny numer ID!")
        return
    for i, t in enumerate(tasks):
        if t["id"] == task_id:
            confirm = input(Fore.RED + f"Czy na pewno chcesz usunąć '{t['title']}'? (t/n): ").lower()
            if confirm == "t":
                removed = tasks.pop(i)
                print(Fore.GREEN + f"🗑️ Zadanie '{removed['title']}' usunięte.")
                log_action("Usunięto zadanie", removed["title"])
            else:
                print(Fore.CYAN + "Anulowano usuwanie.")
            return
    print(Fore.RED + "❌ Nie znaleziono zadania o tym ID.")

def edit_task(tasks):
    """Edytuje tytuł lub priorytet zadania."""
    try:
        task_id = int(input(Fore.YELLOW + "Podaj ID zadania do edycji: "))
    except ValueError:
        print(Fore.RED + "⚠️ Podaj poprawny numer ID!")
        return
    for t in tasks:
        if t["id"] == task_id:
            print(f"Obecny tytuł: {t['title']}")
            new_title = input("Nowy tytuł (Enter by zostawić): ").strip()
            if new_title:
                t["title"] = new_title
            print(f"Obecny priorytet: {t['priority']}")
            new_priority = input("Nowy priorytet (niski/średni/wysoki, Enter by zostawić): ").lower().strip()
            if new_priority in ["niski", "średni", "wysoki"]:
                t["priority"] = new_priority
            print(Fore.GREEN + "✏️ Zadanie zaktualizowane.")
            log_action("Edytowano zadanie", t["title"])
            return
    print(Fore.RED + "❌ Nie znaleziono zadania o tym ID.")

def main_menu():
    """Główna pętla programu."""
    tasks = load_tasks()
    while True:
        print(Fore.CYAN + Style.BRIGHT + "===== PyTask =====")
        print("1️⃣  Dodaj zadanie")
        print("2️⃣  Pokaż wszystkie zadania")
        print("3️⃣  Pokaż tylko aktywne")
        print("4️⃣  Oznacz jako wykonane")
        print("5️⃣  Sortuj/Filtruj zadania")
        print("6️⃣  Edytuj zadanie")
        print("7️⃣  Usuń zadanie")
        print("8️⃣  Zapisz i wyjdź")
        print("=================")
        choice = input(Fore.YELLOW + "Wybierz opcję (1-8): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks, only_active=True)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            sort_and_filter(tasks)
        elif choice == "6":
            edit_task(tasks)
        elif choice == "7":
            delete_task(tasks)
        elif choice == "8":
            save_tasks(tasks)
            print(Fore.GREEN + "💾 Zapisano zmiany. Do zobaczenia!")
            break
        else:
            print(Fore.RED + "⚠️ Nieznana opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main_menu()