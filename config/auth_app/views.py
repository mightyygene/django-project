from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def landing(request):
    return render(request, 'auth_app/landing.html')


@login_required
def home(request):
    return render(request, 'auth_app/home.html')


@login_required
def dashboard(request):
    return render(request, 'auth_app/dashboard.html')


def logout_view(request):
    logout(request)
    return redirect('landing')


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            return render(request, 'auth_app/register.html', {
                'error': 'Passwords do not match'
            })

        if User.objects.filter(email=email).exists():
            return render(request, 'auth_app/register.html', {
                'error': 'Email already exists'
            })

        if User.objects.filter(username=username).exists():
            return render(request, 'auth_app/register.html', {
                'error': 'Username already exists'
            })

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        login(request, user)
        return redirect('dashboard')

    return render(request, 'auth_app/register.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user_obj = User.objects.get(email=email)
            username = user_obj.username
        except User.DoesNotExist:
            return render(request, 'auth_app/login.html', {
                'error': 'User with this email does not exist'
            })

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'auth_app/login.html', {
                'error': 'Invalid password'
            })

    return render(request, 'auth_app/login.html')