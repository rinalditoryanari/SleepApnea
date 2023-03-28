from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')


def index0(request):
    return render(request, 'pages/stisla/dashboard/index-0.html')


def index(request):
    return render(request, 'pages/stisla/dashboard/index.html')

def master(request):
    return render(request, 'pages/stisla/dashboard/master.html')


def superadmin(request):
    return render(request, 'pages/stisla/dashboard/super.html')

def user(request):
    return render(request, 'pages/stisla/dashboard/user.html')