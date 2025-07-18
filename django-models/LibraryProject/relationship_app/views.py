from django.shortcuts import render, get_object_or_404
from .models import Book, Library
from django.views.generic.detail import DetailView
# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get all books in the library
        return context