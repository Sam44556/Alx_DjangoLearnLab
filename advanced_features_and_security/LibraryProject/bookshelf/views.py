from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect
from .models import Book

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
