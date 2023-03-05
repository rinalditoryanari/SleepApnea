from django.shortcuts import render


def utilities_contact(request):
    return render(request, 'pages/utilities-contact.html')


def utilities_invoice(request):
    return render(request, 'pages/utilities-invoice.html')


def utilities_subscribe(request):
    return render(request, 'pages/utilities-subscribe.html')
