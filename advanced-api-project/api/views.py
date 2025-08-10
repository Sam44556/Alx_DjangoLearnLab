
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend


class BookListView(generics.ListAPIView):
    """
    GET /api/books/
    Returns a list of books with filtering, searching, and ordering capabilities.

    Filtering: by title, author__name, publication_year
    Search: text search on title and author__name
    Ordering: by title and publication_year
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Fields available for exact filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Fields to search textually
    search_fields = ['title', 'author__name']

    # Fields allowed for ordering
    ordering_fields = ['title', 'publication_year']

    # Optional: default ordering
    ordering = ['title']
# List all books - accessible to anyone (read-only)



# Retrieve details of one book by ID - accessible to anyone
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book - only authenticated users
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book - only authenticated users
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book - only authenticated users
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
