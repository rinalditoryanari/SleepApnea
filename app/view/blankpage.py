from django.shortcuts import render


def blank_page(request):
    return render(request, 'pages/stisla/blank/blank.html')
