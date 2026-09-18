# 📚 Personal Library Manager

A console-based personal book collection manager built as a Python package.
It stores your library on disk as JSON, so your books are still there the next
time you run the program.

---

## ✨ Features

- ➕ **Add a book** — title, author, year, and genre (with year validation)
- 📖 **View all books** — displayed in a clean, aligned table
- 🔍 **Search books** — by title or author (case-insensitive)
- 🗑️ **Delete a book** — by exact title match
- 📤 **Export to CSV** — save your library to a `.csv` file
- 📥 **Import from CSV** — load books from a `.csv` file
- 🌐 **(Bonus) Online lookup** — fetch a book's author & year from the
  [Open Library API](https://openlibrary.org/developers/api)

---

## 🚀 Setup

Clone the repository

```bash
git clone https://github.com/waseemisaac91/Personal-Library-Manager.git
cd Personal-Library-Manager

When you run python main.py, you'll see this menu:
===== Personal Library Manager =====
1. Add a book
2. View all books
3. Search books
4. Delete a book
5. Export to CSV
6. Import from CSV
7. Exit
Choose an option:
