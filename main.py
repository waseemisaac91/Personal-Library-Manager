"""
main.py
Waseem
"""

import os
from library_app import (
    load_library,
    save_library,
    export_to_csv,
    import_from_csv,
    add_book,
    view_books,
    search_books,
    delete_book,
)

# Optional bonus (may or may not exist depending on team progress)
try:
    from library_app.api_lookup import lookup_book
    API_AVAILABLE = True
except ImportError:
    API_AVAILABLE = False


DATA_FILE = os.path.join("data", "library.json")
CSV_FILE = os.path.join("dara", "library_export.csv")
IMPORT_FILE= os.path.join("data", "books_to_import.csv")


def main_menu():
    """Print the menu and return the user's choice."""



def main():
    """Main loop."""
   
    print("Welcome to your Personal Library Manager! 📚")

    # Load existing library (or start empty)
    books = load_library(DATA_FILE)
    if books:
        print(f"Loaded {len(books)} book(s) from '{DATA_FILE}'.")
    else:
        print("Starting with an empty library.")

    while True:
        choice = main_menu()

        if choice == "1":
            add_book(books)
            save_library(DATA_FILE, books)

        elif choice == "2":
            view_books(books)

        elif choice == "3":
            search_books(books)

        elif choice == "4":
            delete_book(books)
            save_library(DATA_FILE, books)

        elif choice == "5":
            export_to_csv(books, CSV_FILE)

        elif choice == "6":
            imported = import_from_csv(IMPORT_FILE)
            if imported:
                books.extend(imported)
                save_library(DATA_FILE, books)
                print(f"Imported {len(imported)} book(s).")
                print(f"✅ Library now has {len(books)} book(s).")

        elif choice == "7":
            print("Goodbye! 👋")
            break

        else:
            print("⚠️  Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()