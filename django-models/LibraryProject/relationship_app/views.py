from django.shortcuts import render, get_object_or_404
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView,CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()  # Get all books in the library
        return context

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration_app/register.html'