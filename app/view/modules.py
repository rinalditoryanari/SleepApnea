from django.shortcuts import render


def modules_calendar(request):
    return render(request, 'pages/modules-calendar.html')


def modules_chartjs(request):
    return render(request, 'pages/modules-chartjs.html')


def modules_datatables(request):
    return render(request, 'pages/modules-datatables.html')


def modules_flag(request):
    return render(request, 'pages/modules-flag.html')


def modules_font_awesome(request):
    return render(request, 'pages/modules-font-awesome.html')


def modules_ion_icons(request):
    return render(request, 'pages/modules-ion-icons.html')


def modules_owl_carousel(request):
    return render(request, 'pages/modules-owl-carousel.html')


def modules_sparkline(request):
    return render(request, 'pages/modules-sparkline.html')


def modules_sweet_alert(request):
    return render(request, 'pages/modules-sweet-alert.html')


def modules_toastr(request):
    return render(request, 'pages/modules-toastr.html')


def modules_vector_map(request):
    return render(request, 'pages/modules-vector-map.html')


def modules_weather_icon(request):
    return render(request, 'pages/modules-weather-icon.html')
