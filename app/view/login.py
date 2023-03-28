from django.shortcuts import render


def login(request):
    return render(request, 'auth-login-2.html')


def index0(request):
    return render(request, 'pages/stisla/auth/auth-login-2.html')



