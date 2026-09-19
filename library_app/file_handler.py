"""
file_handler.py
Mohamed 
"""

import os
import json
import csv


def load_library(filepath):
    """Load the library from a JSON file. Return a list of books."""
    if not os.path.exists(filepath):
        return[]
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)
            
    except json.JSONDecodeError:
        print("Error: the library file contains invalid JSON.")
        return []
        




def save_library(filepath, books):
    """Save the list of books to a JSON file."""
    folder= os.path.dirname(filepath)
    if folder :
        os.makedirs(folder, exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4, ensure_ascii=False)
    print("Library saved successfully")




def export_to_csv(books, filepath):
    """Export the list of books to a CSV file."""
    fieldnames= ["title", "author", "year", "genre"]
    try:
        folder= os.path.dirname(filepath)
        if folder :
            os.makedirs(folder, exist_ok=True)

        with open(filepath, mode="w", newline="", encoding="utf-8") as file:
            writer= csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)
        print("Books exportes successfully")
    except OSError:
        print("Error: the csv file could not be created.")




def import_from_csv(filepath, existing_books=None):
    """Import books from a CSV file. Return a list of books."""
    
    if existing_books is None:
        existing_books = []

    try:
        with open(filepath, "r", encoding="utf-8", newline="") as f:
            reader = csv.DictReader(f)
            books = []
            for row in reader:
                try:
                    year = int(row.get("year", 0))
                except (ValueError, TypeError):
                    year = row.get("year", "")

                new_book = {
                    "title": (row.get("title") or "").strip(),
                    "author": (row.get("author") or "").strip(),
                    "year": year,
                    "genre": (row.get("genre") or "").strip(),
                }

                # Check for duplicates based on title and author (case-insensitive)
                already_exists = any(
                    b.get("title", "").lower() == new_book["title"].lower()
                    and b.get("author", "").lower() == new_book["author"].lower()
                    for b in existing_books
                )

                if not already_exists:
                    books.append(new_book)

            return books

    except FileNotFoundError:
        print(f"⚠️  File '{filepath}' not found. Nothing imported.")
        return []
    except OSError as e:
        print(f"⚠️  Error: could not read CSV: {e}")
        return []

