from django.shortcuts import render


def data(request):
    return render(request, 'pages/stisla/master/data-akun.html')

def tambahdata(request):
    return render(request, 'pages/stisla/master/tambah-data.html')