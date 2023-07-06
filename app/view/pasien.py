from django.shortcuts import render,redirect
from django.utils import timezone
from app.models import Super,User,Admin,Pasien
from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import mysql.connector as sql
from urllib.parse import unquote
from datetime import date,datetime, timedelta

def editpasien(request,username):
    # email = unquote(username)
    user = User.objects.get(username=username)
    pasien= Pasien.objects.get(username=user.username)
    # pprint(admin)
    # pprint(user)global id,rs,usr,em,pwd
    global id,rs,usr,em,pwd
    username_lama = user.username
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_pasien":
                id=value
            if key=="rs":
                rs=value
            if key=="id_rs":
                id_rs=value
            if key=="name":
                nama=value
            if key=="username":
                usr=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="no_telp":
                telp=value
            if key=="alamat":
                alamat=value    
        
        c="update pasien set id_pasien='{}',rs='{}',id_rs='{}',username='{}',nama_lengkap='{}',alamat='{}',no_telp='{}' where username ='{}' ".format(id,rs,id_rs,usr,nama,alamat,telp,username_lama)
        cursor.execute(c)
        m.commit()
        d="update users set username='{}',email='{}',password='{}' where username ='{}' ".format(usr,em,pwd,username_lama)
        cursor.execute(d)
        m.commit()
        pasiens = Pasien.objects.all()
        messages.success(request,"Data Berhasil diedit !!")
        return render(request, 'pages/stisla/dashboard/pasien.html',{'pasiens':pasiens})
    return render(request, 'pages/stisla/pasien/edit-pasien.html',{'pasien':pasien,'user':user})