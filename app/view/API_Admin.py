from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien,Rekaman
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql
from django import template
from django.core import serializers

username_rs = ''

@csrf_exempt  
def pasien2(request):
    global username_rs,id_rs
    try:
        if request.method=="POST":
            m=sql.connect(host="localhost",user="root",passwd="",database='test')
            cursor=m.cursor()
            d=request.POST
            for key,value in d.items():
                if key=="username_rs":
                    username_rs=value
        d="select id_rs from admin where username='{}'".format(username_rs)
        cursor.execute(d)
        t=tuple(cursor.fetchone())
        a= str(t[0])
        pasiens = Pasien.objects.filter(id_rs=a)
        pasiens = list(pasiens.values())  
        # pprint(a)
        # pprint(pasiens)
        response = {
            'input' :username_rs,
            'pasiens' : pasiens,  
        }
        return JsonResponse(response) 
    except Exception  as e:
        response = {
            'error' : e 
        }
        return JsonResponse(response)
    
@csrf_exempt  
def deteksi(request):
    try:
        if request.method == "POST":
            username_rs = request.POST.get("username_rs")

            # Retrieve id_rs from the database
            m = sql.connect(host="localhost", user="root", passwd="", database="test")
            cursor = m.cursor()
            query = "SELECT id_rs FROM admin WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()

            if result:
                id_rs = result[0]

                # Retrieve pasiens from the Pasien model
                deteksi = Rekaman.objects.filter(id_rs=id_rs).values()

                response = {
                    "input": username_rs,
                    "deteksi": list(deteksi),
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
            query = "SELECT id_rs FROM admin WHERE username = %s"
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
    # return render(request, 'pages/stisla/admin/data-pasien.html',{'pasiens':pasiens})


    # global id_pasien,pwd
    # if request.method=="POST":
    #     m=sql.connect(host="localhost",user="root",passwd="",database='test')
    #     cursor=m.cursor()
    #     d=request.POST
    #     for key,value in d.items():
    #         if key=="id_pasien":
    #             id_pasien=value
        
    #     c="select * from pasien where id_pasien='{}'".format(id_pasien)
    #     cursor.execute(c)
    #     try:
    #         t=tuple(cursor.fetchone())
    #         a= str(t[3])            
    #         response = {
    #             'nama_lengkap' : str(t[4]),  
    #         }
    #         return JsonResponse(response) 
    #     except Exception  as e:
    #         response = {
    #             'error' : "Id tidak ditemukan" 
    #         }
    #         return JsonResponse(response)