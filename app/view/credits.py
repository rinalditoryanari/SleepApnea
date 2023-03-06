from django.shortcuts import render


def credits(request):
    return render(request, 'pages/stisla/credits/credits.html')
