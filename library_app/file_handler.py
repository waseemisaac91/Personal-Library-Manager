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




def import_from_csv(filepath):
    """Import books from a CSV file. Return a list of books."""
    imported_books =[]
    try:
        with open(filepath, mode="r", newline="", encoding="utf-8") as file:
            reder= csv.DictReader(file)
            for row in reder:
                book={"title":row["title"],"author": row["author"],
                      "year": int(row["year"]), "genre":row["genre"]}
                imported_books.append(book)
                print("ROW:", row)
        print("Books imported successfully")
        
        return imported_books
        
    except FileNotFoundError:
        print("Error: csv file not found.")
        return []
    except ValueError:
        print("Error: one of the year in csv file is invalid.")
        return []
    except KeyError:
        print("Error: the csv file has incorrect column names.")
        return []

