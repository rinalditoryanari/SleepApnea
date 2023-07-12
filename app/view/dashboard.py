from django.shortcuts import render
from app.models import Super,User,Rekaman,Pasien


def dashboard(request):
    return render(request, 'dashboard.html')


def index0(request):
    return render(request, 'pages/stisla/dashboard/index-0.html')


def index(request):
    return render(request, 'pages/stisla/dashboard/index.html')

def master(request):
    supers = User.objects.filter(role="super").count()
    hospitals = Super.objects.values('rs').distinct().count()
    masters = User.objects.filter(role="master")
    masters_list = list(masters.values())
    masters_data = []
    for master in masters_list:
        masters_data.append({
            'email': master['email'],
            'role': master['role'],
            'username': master['username']
        })
    hasil = {
        'supers': supers,
        'hospitals': hospitals,
        'masters': masters_data,  # Pass the updated masters data
    }
    return render(request, 'pages/stisla/dashboard/master.html',hasil)


def superadmin(request):
    return render(request, 'pages/stisla/dashboard/super.html')

def admin(request):
    return render(request, 'pages/stisla/dashboard/admin.html')

def pasien(request):
    return render(request, 'pages/stisla/dashboard/pasien.html')