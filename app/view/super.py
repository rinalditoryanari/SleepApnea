from django.shortcuts import render,redirect
from django.utils import timezone
from app.models import Super,User,Admin,Pasien,Rekaman
from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import mysql.connector as sql
from datetime import date,datetime, timedelta


id=''
rs=''
usr=''
em=''
pwd=''
nama=''
id_rs=''
tgl_lahir=''
jk=''
telp=''
alamat=''
now = timezone.now()

def data(request):
    admins = Admin.objects.all()
    return render(request, 'pages/stisla/super/data-akun.html',{'admins':admins})

def tambahdata(request):
    global id,rs,usr,em,pwd,tgl_lahir,jk,telp,alamat
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
            if key=="tgl_lahir":
                tgl_lahir=value
            if key=="jenis_kelamin":
                jk=value
            if key=="no_telp":
                telp=value
            if key=="alamat":
                alamat=value
        tgl = datetime.strptime(tgl_lahir,"%Y-%m-%d")
        today = datetime.now()
        age = today - tgl
        age_year = age.days // 365
        c="insert into users Values('{}','{}','{}','{}')".format(usr,em,pwd,"admin")
        cursor.execute(c)
        m.commit()
        d="insert into admin Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id,rs,id_rs,usr,nama,now,tgl_lahir,age_year,jk,alamat,telp)
        cursor.execute(d)
        m.commit()
        admins= Admin.objects.all()
        messages.success(request,"Data Berhasil ditambah !!")
        return render(request, 'pages/stisla/super/data-akun.html',{'admins':admins})
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
            if key=="no_telp":
                telp=value
            if key=="alamat":
                alamat=value
        c="update admin set id_admin='{}',rs='{}',id_rs='{}',username='{}',nama_lengkap='{}',alamat='{}',no_telp='{}' where username ='{}' ".format(id,rs,id_rs,usr,nama,alamat,telp,username_lama)
        cursor.execute(c)
        m.commit()
        d="update users set username='{}',email='{}',password='{}' where username ='{}' ".format(usr,em,pwd,username_lama)
        cursor.execute(d)
        m.commit()
        admins = Admin.objects.all()
        messages.success(request,"Data Berhasil diedit !!")
        return render(request, 'pages/stisla/super/data-akun.html',{'admins':admins})
    return render(request, 'pages/stisla/super/edit-data.html',{'admin':admin,'user':user})

def destroy(request, id_admin): 
    admin = Admin.objects.get(id_admin=id_admin)
    user = User.objects.get(username=admin.username)
    # pprint(admin)
    admin.delete()
    user.delete()
    admins = Admin.objects.all()
    messages.success(request,"Data Berhasil dihapus !!")
    return render(request, 'pages/stisla/super/data-akun.html',{'admins':admins})
    

def insertpasien(request):
    global id,rs,usr,em,pwd
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
            if key=="tgl_lahir":
                tgl_lahir=value
            if key=="jenis_kelamin":
                jk=value
            if key=="no_telp":
                telp=value
            if key=="alamat":
                alamat=value
        tgl = datetime.strptime(tgl_lahir,"%Y-%m-%d")
        today = datetime.now()
        age = today - tgl
        age_year = age.days // 365
        c="insert into users Values('{}','{}','{}','{}')".format(usr,em,pwd,"pasien")
        cursor.execute(c)
        m.commit()
        d="insert into pasien Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id,rs,id_rs,usr,nama,now,tgl_lahir,age_year,jk,alamat,telp)
        cursor.execute(d)
        m.commit()
        pasiens= Pasien.objects.all()
        messages.success(request,"Data Berhasil ditambah !!")
        return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})
    return render(request, 'pages/stisla/super/tambah-pasien.html')

def pasien(request):
    pasiens = Pasien.objects.all()
    return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})

def editpasien(request,id_pasien):
    pasien= Pasien.objects.get(id_pasien=id_pasien)
    user = User.objects.get(username=pasien.username)
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
        return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})
    return render(request, 'pages/stisla/super/edit-pasien.html',{'pasien':pasien,'user':user})

def hapuspasien(request, id_pasien): 
    pasien= Pasien.objects.get(id_pasien=id_pasien)
    user = User.objects.get(username=pasien.username)
    # pprint(admin)
    pasien.delete()
    user.delete()
    pasiens = Pasien.objects.all()
    messages.success(request,"Data Berhasil dihapus !!") 
    return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})

def simpan_deteksi(request):
    global id_pasien,sinyal,jenis
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_pasien":
                id_pasien=value
            if key=="jenis_fisiologis":
                sinyal=value
            if key=="result":
                hasil=value      
        c="select * from pasien where id_pasien='{}'".format(id_pasien)
        cursor.execute(c)
        t=tuple(cursor.fetchone())
        usia= str(t[7])
        nama_lengkap = str(t[4])
        d="insert into rekaman Values('{}','{}','{}','{}','{}','{}')".format(id_pasien,nama_lengkap,usia,now,hasil,sinyal)
        cursor.execute(d)
        m.commit()
        rekamans= Rekaman.objects.all()
        messages.success(request,"Data Berhasil ditambah !!")
        return render(request, 'pages/stisla/super/riwayat-laporan.html',{'rekamans':rekamans})
    return render(request, 'pages/stisla/super/tambah-rekaman.html')
        
            

def tambahpasien(request):
    return render(request, 'pages/stisla/super/tambah-pasien.html')

def riwayatlaporan(request):
    rekamans= Rekaman.objects.all()
    return render(request, 'pages/stisla/super/riwayat-laporan.html',{'rekamans':rekamans})

def tambahrekaman(request):
    return render(request, 'pages/stisla/super/tambah-rekaman.html')