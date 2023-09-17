from django.shortcuts import render
from app.models import Super,User,Rekaman,Pasien

def landingpage(request):
    return render(request, 'pages/stisla/landing/landing-page.html')