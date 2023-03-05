from django.shortcuts import render


def error_403(request):
    return render(request, 'pages/errors-403.html')


def error_404(request):
    return render(request, 'pages/errors-404.html')


def error_500(request):
    return render(request, 'pages/errors-500.html')


def error_503(request):
    return render(request, 'pages/errors-503.html')
