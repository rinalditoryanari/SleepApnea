from django.shortcuts import render


def auth_forgot_password(request):
    return render(request, 'pages/auth-forgot-password.html')


def auth_login(request):
    return render(request, 'pages/auth-login.html')


def auth_login2(request):
    return render(request, 'pages/auth-login2.html')


def auth_register(request):
    return render(request, 'pages/auth-register.html')


def auth_reset_password(request):
    return render(request, 'pages/auth-reset-password.html')
