from django.shortcuts import render
from django.http import JsonResponse
from app.models import Super,User,Admin,Pasien
from django.views.decorators.csrf import csrf_exempt
import mysql.connector as sql
from django import template

em=''
pwd=''

def login(request):
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
        t=tuple(cursor.fetchone())
        a= str(t[3])
        if t==():
            return render(request,'pages/stisla/auth/auth-login-2.html')
        else:
            if a=='master':
                return render(request,"pages/stisla/dashboard/master.html")
            elif a=='super':
                return render(request,"pages/stisla/dashboard/super.html")
            elif a=='admin':
                return render(request,"pages/stisla/dashboard/admin.html")
            elif a=='pasien':
                usr = str(t[0])
                user = User.objects.get(username=usr)
                pasiens = Pasien.objects.get(username=user.username)
                return render(request,"pages/stisla/dashboard/pasien.html",{'pasiens':pasiens,'user':user})
    return render(request, 'pages/stisla/auth/auth-login-2.html')

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
        t=tuple(cursor.fetchone())
        a= str(t[3])
        if t==():
            url= 'http://127.0.0.1:8000/pages/stisla/auth/auth-login-2.html'
        else:
            if a=='master':
                url = "http://127.0.0.1:8000/pages/stisla/dashboard/master.html"
            elif a=='super':
                url = "http://127.0.0.1:8000/pages/stisla/dashboard/super.html"
            elif a=='admin':
                url = "http://127.0.0.1:8000/pages/stisla/dashboard/admin.html"
            elif a=='pasien':
                url = "http://127.0.0.1:8000/pages/stisla/dashboard/pasien.html"
    url = 'http://127.0.0.1:8000/pages/stisla/auth/auth-login-2.html'
    response = {
        'username' : str(t[0]),
        'email'     : str(t[1]),
        'role' : str(t[3]),
        'url' : url 
    }
    return JsonResponse


def index0(request):
    return render(request, 'pages/stisla/auth/auth-login-2.html')


# Create your views here.



# def loginaction(request):
#     global em,pwd
#     if request.method=="POST":
#         m=sql.connect(host="localhost",user="root",passwd="vivek",database='website')
#         cursor=m.cursor()
#         d=request.POST
#         for key,value in d.items():
#             if key=="email":
#                 em=value
#             if key=="password":
#                 pwd=value
        
#         c="select * from users where email='{}' and password='{}'".format(em,pwd)
#         cursor.execute(c)
#         t=tuple(cursor.fetchall())
#         if t==():
#             return render(request,'error.html')
#         else:
#             return render(request,"welcome.html")

#     return render(request,'login_page.html')

