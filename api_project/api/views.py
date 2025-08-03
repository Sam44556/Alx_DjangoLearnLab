from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from django_filters.rest_framework import DjangoFilterBackend

class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__name', 'publisher__name', 'published_date']  # filtering with query params

    def get_queryset(self):
        return Book.objects.select_related('author', 'publisher') 