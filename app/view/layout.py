from django.shortcuts import render

# Create your views here.


def layout_default_layout(request):
    return render(request, 'pages/stisla/layout/layout-default-layout.html')


def layout_top_navigation(request):
    return render(request, 'pages/stisla/layout/layout-top-navigation.html')


def layout_transparent(request):
    return render(request, 'pages/stisla/layout/layout-transparent.html')
