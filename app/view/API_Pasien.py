from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien,Rekaman
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql
from django import template


@csrf_exempt
def cekid_pasien(request):
    global id_pasien,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_pasien":
                id_pasien=value
        
        c="select * from pasien where id_pasien='{}'".format(id_pasien)
        cursor.execute(c)
        try:
            t=tuple(cursor.fetchone())
            a= str(t[3])            
            response = {
                'nama_lengkap' : str(t[4]),  
            }
            return JsonResponse(response) 
        except Exception  as e:
            response = {
                'error' : "Id tidak ditemukan" 
            }
            return JsonResponse(response)

@csrf_exempt  
def ceknama_pasien(request):
    global id_pasien,nama_lengkap
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="nama":
                nama_lengkap=value
        
        c="select * from pasien where nama_lengkap='{}'".format(nama_lengkap)
        cursor.execute(c)
        try:
            t=tuple(cursor.fetchone())
            a= str(t[3])            
            response = {
                'id_pasien' : str(t[0]),  
            }
            return JsonResponse(response) 
        except Exception  as e:
            response = {
                'error' : "User tidak ditemukan" 
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
            query = "SELECT nama_lengkap FROM pasien WHERE username = %s"
            cursor.execute(query, (username_rs,))
            result = cursor.fetchone()

            if result:
                nama_lengkap = result[0]

                # Retrieve pasiens from the Pasien model
                deteksi = Rekaman.objects.filter(nama_lengkap=nama_lengkap).values()

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


     
        
