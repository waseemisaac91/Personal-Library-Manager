"""
book_operations.py
By Dana
"""


def add_book(books):
    """Ask the user for book details and append to books (in-place)."""
    title = input("Title: ").strip()
    if not title:
        print("⚠️  Title cannot be empty.")
        return
    author = input("Author: ").strip()
    if not author:
        print("⚠️  Author cannot be empty.")
        return
    while True:
        year_input = input("Year: ").strip()
        try:
            year = int(year_input)
            break
        except ValueError:
            print("⚠️  Please enter a valid number for the year.")
    genre = input("Genre: ").strip()

    books.append({"title": title, "author": author, "year": year, "genre": genre})
    print("✅ Book added and saved!")


def view_books(books):
    """Print every book in a readable, aligned format."""
    if not books:
        print("\n📚 Your library is empty. Add a book to get started!")
        return
    
    print(f"\n--- Your Library ({len(books)} book{'s' if len(books) != 1 else ''}) ---")
    print(f"{'Title':<25}{'Author':<25}{'Year':<8}{'Genre'}")
    print("-" * 75)

    for book in books:
        print(f"{book.get('title', ''):<25}{book.get('author', ''):<25}{str(book.get('year', '')):<8}{book.get('genre', '')}")


def search_books(books):
    """Search books by title or author (case-insensitive) and print matches."""
    if not books:
        print("\n📚 Your library is empty. Nothing to search.")
        return
    term = input("Enter title or author to search: ").strip().lower()
    matches = [
        b for b in books
        if term in b.get("title", "").lower()
        or term in b.get("author", "").lower()
    ]

    if not matches:
        print(f"🔍 No books found matching '{term}'.")
        return
    for book in matches:

        print(f"  • {book.get('title')} — {book.get('author')} ...")


def delete_book(books):
    """Ask for a title and remove the matching book (in-place)."""
    if not books:
        print("\n📚 Your library is empty. Nothing to delete.")
        return
    title = input("Enter the title of the book to delete: ").strip()
    for i, book in enumerate(books):
        if book.get("title", "").lower() == title.lower():
            removed = books.pop(i)
            print(f"🗑️  Deleted '{removed.get('title')}'")
            return
        
    print(f"⚠️  No book found with the title '{title}'.")