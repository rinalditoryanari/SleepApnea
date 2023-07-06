from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql
from django import template

em=''
pwd=''

@csrf_exempt
def loginAPI(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        
        c="select * from users where email='{}' and password='{}'".format(em,pwd)
        cursor.execute(c)
        try:
            t=tuple(cursor.fetchone())
            a= str(t[3])
            if t==():
                url = 'http://127.0.0.1:8000/auth-login2'
                response = {
                    'url' : 'url '
                }
                return JsonResponse(response)
            else:
                if a=='master':
                    url = "http://127.0.0.1:8000/dashboard-master"
                elif a=='super':
                    url = "http://127.0.0.1:8000/dashboard-super"
                elif a=='admin':
                    url = "http://127.0.0.1:8000/dashboard-admin"
                elif a=='pasien':
                    url = "http://127.0.0.1:8000/dashboard-pasien"
                response = {
                    'username' : str(t[0]),
                    'email'     : str(t[1]),
                    'role' : str(t[3]),
                    'url' : url    
                }
                return JsonResponse(response) 
        except Exception  as e:
            url = 'http://127.0.0.1:8000/auth-login2'
            response = {
                'url' : url 
            }
            return JsonResponse(response)
