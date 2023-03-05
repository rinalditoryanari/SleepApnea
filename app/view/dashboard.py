from django.shortcuts import render


def dashboard(request):
    return render(request, 'dashboard.html')


def index0(request):
    return render(request, 'pages/index-0.html')


def index(request):
    return render(request, 'pages/index.html')
