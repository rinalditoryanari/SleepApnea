from django.shortcuts import render


def data(request):
    return render(request, 'pages/stisla/super/data-akun.html')

def tambahdata(request):
    return render(request, 'pages/stisla/super/tambah-data.html')

def pasien(request):
    return render(request, 'pages/stisla/super/data-pasien.html')

def tambahpasien(request):
    return render(request, 'pages/stisla/super/tambah-pasien.html')

def riwayatlaporan(request):
    return render(request, 'pages/stisla/super/riwayat-laporan.html')

def tambahrekaman(request):
    return render(request, 'pages/stisla/super/tambah-rekaman.html')