from django.shortcuts import render,redirect
from django.utils import timezone
from app.models import Super,User,Admin 
from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect
import mysql.connector as sql

id=''
rs=''
usr=''
em=''
pwd=''
nama=''
id_rs=''
now = timezone.now()

def data(request):
    admins = Admin.objects.all()
    return render(request, 'pages/stisla/super/data-akun.html',{'admins':admins})

def tambahdata(request):
    global id,rs,usr,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_admin":
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
        
        c="insert into users Values('{}','{}','{}','{}')".format(usr,em,pwd,"admin")
        cursor.execute(c)
        m.commit()
        d="insert into admin Values('{}','{}','{}','{}','{}','{}')".format(id,rs,id_rs,usr,nama,now)
        cursor.execute(d)
        m.commit()
        admin= Admin.objects.all()
        return render(request, 'pages/stisla/super/data-akun.html',{'admin':admin})
    return render(request, 'pages/stisla/super/tambah-data.html')

def editdata(request,id_admin):
    admin= Admin.objects.get(id_admin=id_admin)
    user = User.objects.get(username=admin.username)
    # pprint(admin)
    # pprint(user)global id,rs,usr,em,pwd
    global id,rs,usr,em,pwd
    username_lama = user.username
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_admin":
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
        
        c="update admin set id_admin='{}',rs='{}',id_rs='{}',username='{}',nama_lengkap='{}' where username ='{}' ".format(id,rs,id_rs,usr,nama,username_lama)
        cursor.execute(c)
        m.commit()
        d="update users set username='{}',email='{}',password='{}' where username ='{}' ".format(usr,em,pwd,username_lama)
        cursor.execute(d)
        m.commit()
        admins = Admin.objects.all()
        return render(request, 'pages/stisla/super/data-akun.html',{'admins':admins})
    return render(request, 'pages/stisla/super/edit-data.html',{'admin':admin,'user':user})

def destroy(request, id_admin): 
    admin = Admin.objects.get(id_admin=id_admin)
    user = User.objects.get(username=admin.username)
    # pprint(admin)
    admin.delete()
    user.delete() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def pasien(request):
    return render(request, 'pages/stisla/super/data-pasien.html')

def tambahpasien(request):
    return render(request, 'pages/stisla/super/tambah-pasien.html')

def riwayatlaporan(request):
    return render(request, 'pages/stisla/super/riwayat-laporan.html')

def tambahrekaman(request):
    return render(request, 'pages/stisla/super/tambah-rekaman.html')