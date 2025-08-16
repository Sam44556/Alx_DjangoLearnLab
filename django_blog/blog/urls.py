from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # Auth (built-in for login/logout)
    path('login/',  auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Custom
    path("", PostListView.as_view(), name="post-list"),
    path("post/new/", PostCreateView.as_view(), name="post-create"),
    path("post/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path("post/<int:pk>/update/", PostUpdateView.as_view(), name="post-update"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path("posts/", PostListView.as_view(), name="post-list"),
    path("post/<int:pk>/comments/new/" ,views.add_comment, name="add_comment"),
    path('comment/new/', CommentCreateView.as_view(), name='comment-create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment-delete'),
    path("search/", views.search_posts, name="post-search"),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name="posts-by-tag"),
]
   

