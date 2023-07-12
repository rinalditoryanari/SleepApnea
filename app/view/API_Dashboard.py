from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien,Rekaman
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql
from django import template
from django.core import serializers
from datetime import datetime, date
from django.utils import timezone

@csrf_exempt  
def superadmin(request):
    try:
        if request.method == "POST":
            username_rs = request.POST.get("username_rs")
            print(username_rs)
            # Retrieve id_rs from the database
            m = sql.connect(host="localhost", user="root", passwd="", database="test")
            cursor = m.cursor()
            query = "SELECT id_rs FROM super WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()
            
            if result:
                id_rs = str(result[0])

                # Retrieve pasiens from the Pasien model
                admins = Admin.objects.filter(id_rs=id_rs).count()
                pasiens = Pasien.objects.filter(id_rs=id_rs).count()
                supers = Super.objects.filter(username=username_rs).values()
                response = {
                    "input": username_rs,
                    "admins": admins,
                    "pasiens" : pasiens,
                    "supers" : list(supers.values())
                }
                return JsonResponse(response)
            else:
                response = {
                    "error": "Invalid username_rs",
                }
                return JsonResponse(response, status=400)
        else:
            response = {
                "error": "Invalid request method",
            }
            return JsonResponse(response, status=400)
    except Exception as e:
        response = {
            "error": str(e),
        }
        return JsonResponse(response, status=500)
    

@csrf_exempt  
def admin(request):
    try:
        if request.method == "POST":
            username_rs = request.POST.get("username_rs")
            print(username_rs)
            # Retrieve id_rs from the database
            m = sql.connect(host="localhost", user="root", passwd="", database="test")
            cursor = m.cursor()
            query = "SELECT id_rs FROM admin WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()
            
            if result:
                id_rs = str(result[0])

                # Retrieve pasiens from the Pasien model
                rekamans = Rekaman.objects.filter(id_rs=id_rs).count()
                pasiens = Pasien.objects.filter(id_rs=id_rs).count()
                admins = Admin.objects.filter(username=username_rs).values()
                # Get the current date
                today = date.today()
                # Filter the records based on the datetime field
                start_of_day = timezone.make_aware(datetime.combine(today, datetime.min.time()))
                end_of_day = timezone.make_aware(datetime.combine(today, datetime.max.time()))
                rekamans_today = Rekaman.objects.filter(waktu_rekaman__range=(start_of_day, end_of_day)).count()

                response = {
                    "input": username_rs,
                    "rekamans": rekamans,
                    "pasiens" : pasiens,
                    "admins" : list(admins.values()),
                    "rekamans_today" : rekamans_today,
                }
                return JsonResponse(response)
            else:
                response = {
                    "error": "Invalid username_rs",
                }
                return JsonResponse(response, status=400)
        else:
            response = {
                "error": "Invalid request method",
            }
            return JsonResponse(response, status=400)
    except Exception as e:
        response = {
            "error": str(e),
        }
        return JsonResponse(response, status=500)
    
@csrf_exempt  
def pasien(request):
    try:
        if request.method == "POST":
            username_rs = request.POST.get("username_rs")
            print(username_rs)
            # Retrieve id_rs from the database
            m = sql.connect(host="localhost", user="root", passwd="", database="test")
            cursor = m.cursor()
            query = "SELECT nama_lengkap FROM pasien WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()
            
            if result:
                nama_lengkap = str(result[0])

                # Retrieve pasiens from the Pasien model
                rekamans = Rekaman.objects.filter(nama_lengkap=nama_lengkap).count()
                pasiens = Pasien.objects.filter(username=username_rs).values()
                # Get the current date
                today = date.today()
                # Filter the records based on the datetime field
                start_of_day = timezone.make_aware(datetime.combine(today, datetime.min.time()))
                end_of_day = timezone.make_aware(datetime.combine(today, datetime.max.time()))
                rekamans_today = Rekaman.objects.filter(nama_lengkap=nama_lengkap).filter(waktu_rekaman__range=(start_of_day, end_of_day)).count()

                response = {
                    "input": username_rs,
                    "rekamans": rekamans,
                    "pasiens" : list(pasiens.values()),
                    "rekamans_today" : rekamans_today,
                }
                return JsonResponse(response)
            else:
                response = {
                    "error": "Invalid username_rs",
                }
                return JsonResponse(response, status=400)
        else:
            response = {
                "error": "Invalid request method",
            }
            return JsonResponse(response, status=400)
    except Exception as e:
        response = {
            "error": str(e),
        }
        return JsonResponse(response, status=500)