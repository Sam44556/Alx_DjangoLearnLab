from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book
from .forms import ExampleForm
def books(request):
    all_books = Book.objects.all()
    return render(request, 'bookshelf/books.html', {'books': all_books})
def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        title = form.cleaned_data['title']
        results = Book.objects.filter(title__icontains=title)
def exampleform(request):
    form = ExampleForm()
    return render(request, 'relationship_app/form_example.html', {'form': form})

@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    # logic to add book
    return render(request, 'add_book.html')

@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, book_id):
    # logic to edit book
    return render(request, 'edit_book.html')

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, book_id):
    # logic to delete book
    return redirect('book_list')
