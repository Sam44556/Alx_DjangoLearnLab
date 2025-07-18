import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author = Author.objects.get(name='John Doe')
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print(f"- {book.title}")

# 2. List all books in a library
library = Library.objects.get(name='Main Library')
print(f"\nBooks in {library.name}:")
for book in library.books.all():
    print(f"- {book.title}")

# 3. Retrieve the librarian for a library
library = Library.objects.get(name='library_name')
try:
    librarian = library.librarian
    print(f"\nLibrarian of {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"{library.name} has no assigned librarian.")
