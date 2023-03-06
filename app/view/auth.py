from django.shortcuts import render


def auth_forgot_password(request):
    return render(request, 'pages/stisla/auth/auth-forgot-password.html')


def auth_login(request):
    return render(request, 'pages/stisla/auth/auth-login.html')


def auth_login2(request):
    return render(request, 'pages/stisla/auth/auth-login2.html')


def auth_register(request):
    return render(request, 'pages/stisla/auth/auth-register.html')


def auth_reset_password(request):
    return render(request, 'pages/stisla/auth/auth-reset-password.html')
