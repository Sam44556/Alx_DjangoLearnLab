from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Show these columns
    list_filter = ('publication_year', 'author')            # Add sidebar filters
    search_fields = ('title', 'author') 