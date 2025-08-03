from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer

from rest_framework.permissions import IsAuthenticated

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics

class BookList(generics.ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]  # Only admin users can access this view
    queryset = Book.objects.all()
    serializer_class = BookSerializer
      # Only logged-in users can access

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
