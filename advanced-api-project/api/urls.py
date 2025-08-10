from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateNoPKView, BookDeleteNoPKView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/update/', BookUpdateNoPKView.as_view(), name='book-update-no-pk'),
    path('books/delete/', BookDeleteNoPKView.as_view(), name='book-delete-no-pk'),
]
