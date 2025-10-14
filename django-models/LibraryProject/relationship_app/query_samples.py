import os
import django

# Setup Django environment (only needed if running this file directly)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# --- Example data setup (optional for first run) ---
if not Author.objects.exists():
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="J.K. Rowling")

    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Harry Potter", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library1.books.add(book1, book2)

    library2 = Library.objects.create(name="Community Library")
    library2.books.add(book3)

    Librarian.objects.create(name="Alice", library=library1)
    Librarian.objects.create(name="Bob", library=library2)


# --- Queries ---
# 1️⃣ All books by a specific author
objects.filter(author=author)
author_name = "George Orwell"
Author.objects.get(name=author_name).exists()
object.filter(author=author)
books_by_author = Book.objects.filter(author_author=author_name)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# 2️⃣ All books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
print(f"Books in {library_name}: {[book.title for book in library.books.all()]}")

# 3️⃣ Retrieve the librarian for a library
librarian = library.librarian
print(f"Librarian for {library_name}: {librarian.name}")

