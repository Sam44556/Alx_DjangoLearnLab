from django.shortcuts import render
from .models import Post

def home(request):
    posts = Post.objects.order_by('-published_date')[:10]
    return render(request, 'blog/home.html', {'posts': posts})