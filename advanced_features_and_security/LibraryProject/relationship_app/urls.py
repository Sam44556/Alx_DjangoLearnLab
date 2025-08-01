from django.urls import path
from .views import list_books, LibraryDetailView , Register, add_book, edit_book, delete_book
from django.contrib.auth.decorators import permission_required, user_passes_test
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from . import views
from .views import Register 

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/',views.member_view, name='member_view'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit_book/<int:book_id>/', views.edit_book, name='edit_book'),
    path('delete/<int:pk>/', views.delete_book, name='delete-book'),
]
