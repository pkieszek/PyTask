import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Wczytuje listę zadań z pliku JSON, jeśli istnieje."""
    if not os.path.exists(TASKS_FILE):
        return []
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("❌ Błąd w pliku JSON. Tworzę nową listę zadań.")
        return []

def save_tasks(tasks):
    """Zapisuje listę zadań do pliku JSON."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)

def add_task(tasks):
    """Dodaje nowe zadanie do listy."""
    title = input("📌 Podaj nazwę zadania: ").strip()
    if not title:
        print("⚠️ Nazwa nie może być pusta!")
        return
    priority = input("Priorytet (niski/średni/wysoki): ").lower().strip()
    if priority not in ["niski", "średni", "wysoki"]:
        priority = "średni"
    new_task = {
        "id": len(tasks) + 1,
        "title": title,
        "priority": priority,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    tasks.append(new_task)
    print("✅ Zadanie dodane!")

def show_tasks(tasks, only_active=False):
    """Wyświetla listę zadań."""
    filtered = [t for t in tasks if not t["done"]] if only_active else tasks
    if not filtered:
        print("📭 Brak zadań do wyświetlenia.")
        return
    print("\n===== LISTA ZADAŃ =====")
    for t in filtered:
        status = "✅" if t["done"] else "❌"
        print(f"[{t['id']}] {status} {t['title']} ({t['priority']}) - utworzono {t['created']}")
    print("========================\n")

def mark_done(tasks):
    """Oznacza zadanie jako wykonane."""
    try:
        task_id = int(input("Podaj ID zadania do oznaczenia jako wykonane: "))
    except ValueError:
        print("⚠️ Podaj poprawny numer ID!")
        return
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            print(f"🟢 Zadanie '{t['title']}' oznaczone jako wykonane.")
            return
    print("❌ Nie znaleziono zadania o tym ID.")

def main_menu():
    """Główna pętla programu."""
    tasks = load_tasks()
    while True:
        print("===== PyTask =====")
        print("1️⃣  Dodaj zadanie")
        print("2️⃣  Pokaż wszystkie zadania")
        print("3️⃣  Pokaż tylko aktywne")
        print("4️⃣  Oznacz jako wykonane")
        print("5️⃣  Zapisz i wyjdź")
        print("=================")
        choice = input("Wybierz opcję (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks, only_active=True)
        elif choice == "4":
            mark_done(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("💾 Zapisano zmiany. Do zobaczenia!")
            break
        else:
            print("⚠️ Nieznana opcja, spróbuj ponownie.")

if __name__ == "__main__":
    main_menu()