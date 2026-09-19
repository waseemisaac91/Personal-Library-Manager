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
    
    print("1. Add a book")
    print("2. View all books")
    print("3. Search books")
    print("4. Delete a book")
    print("5. Export to CSV")
    print("6. Import from CSV")
    print("7. Exit")

    return input("Choose an option: ").strip()


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
              imported = import_from_csv(CSV_FILE, existing_books=books)
              if imported:
               books.extend(imported)
               save_library(DATA_FILE, books)
               
               print(f"✅ Added {len(imported)} new book(s).")

              else:
               print("⚠️  No new books to import (all already exist).")

        elif choice == "7":
            print("Goodbye! 👋")
            break

        else:
            print("⚠️  Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
