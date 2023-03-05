from django.shortcuts import render


def credits(request):
    return render(request, 'pages/credits.html')
