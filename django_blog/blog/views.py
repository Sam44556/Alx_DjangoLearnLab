from django.shortcuts import render
from .models import Post
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import RegisterForm

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user: User = form.save(commit=False)
            user.username = user.username.lower()
            user.email = user.email.lower()
            user.save()
            login(request, user)  # auto-login after register
            messages.success(request, 'Account created and logged in.')
            return redirect('home')
        messages.error(request, 'Please fix the errors below.')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').lower()
        first = request.POST.get('first_name', '')
        last = request.POST.get('last_name', '')

        if email and User.objects.exclude(pk=request.user.pk).filter(email__iexact=email).exists():
            messages.error(request, 'Email already in use.')
        else:
            request.user.email = email
            request.user.first_name = first
            request.user.last_name = last
            request.user.save()
            messages.success(request, 'Profile updated.')
        return redirect('profile')

    return render(request, 'registration/profile.html')

