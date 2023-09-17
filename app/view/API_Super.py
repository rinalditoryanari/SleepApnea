from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql
from django import template
from django.core import serializers

username_rs = ''

@csrf_exempt  
def admin(request):
    try:
        if request.method == "POST":
            username_rs = request.POST.get("username_rs")

            # Retrieve id_rs from the database
            m = sql.connect(host="localhost", user="root", passwd="", database="test")
            cursor = m.cursor()
            query = "SELECT id_rs FROM super WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()

            if result:
                id_rs = result[0]

                # Retrieve pasiens from the Pasien model
                admins = Admin.objects.filter(id_rs=id_rs).values()

                response = {
                    "input": username_rs,
                    "admins": list(admins),
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

            # Retrieve id_rs from the database
            m = sql.connect(host="localhost", user="root", passwd="", database="test")
            cursor = m.cursor()
            query = "SELECT id_rs FROM super WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()

            if result:
                id_rs = result[0]

                # Retrieve pasiens from the Pasien model
                pasiens = Pasien.objects.filter(id_rs=id_rs).values()

                response = {
                    "input": username_rs,
                    "pasiens": list(pasiens),
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