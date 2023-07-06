from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien
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
        
