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

DATA_FILE = os.path.join("data", "library.json")
CSV_FILE = "library_export.csv"


def main_menu():
    """Print the menu and return the user's choice."""
    pass


def main():
    """Main loop."""
    pass


if __name__ == "__main__":
    main()