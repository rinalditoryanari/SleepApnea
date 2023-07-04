from django.shortcuts import render,redirect
from django.utils import timezone
from app.models import Super,User 
from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from datetime import date,datetime, timedelta
import mysql.connector as sql

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
    supeer= Super.objects.all()
    pprint(supeer)
    # data = {
    #     'name': 'John Doe',
    #     'age': 30,
    #     'email': 'johndoe@example.com'
    # }
    # pprint(data)
    # return HttpResponse("Data printed in console. Check the console output.")
    return render(request, 'pages/stisla/master/data-akun.html',{'supeer':supeer})

def tambahdata(request):
    return render(request, 'pages/stisla/master/tambah-data.html')

def editdata(request,id_nurse):
    super= Super.objects.get(id_nurse=id_nurse)
    user = User.objects.get(username=super.username)
    # pprint(user)global id,rs,usr,em,pwd
    global id,rs,usr,em,pwd,tgl_lahir,jk,telp,alamat
    username_lama = user.username
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_nurse":
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
        c="update super set id_nurse='{}',rs='{}',id_rs='{}',username='{}',nama_lengkap='{}',alamat='{}',no_telp='{}' where username ='{}' ".format(id,rs,id_rs,usr,nama,alamat,telp,username_lama)
        cursor.execute(c)
        m.commit()
        d="update users set username='{}',email='{}',password='{}' where username ='{}' ".format(usr,em,pwd,username_lama)
        cursor.execute(d)
        m.commit()
        supeer = Super.objects.all()
        messages.success(request,"Data Berhasil diedit !!")
        return render(request, 'pages/stisla/master/data-akun.html',{'supeer':supeer})
    return render(request, 'pages/stisla/master/edit-data.html',{'super':super,'user':user})

def destroy(request, id_nurse): 
    super = Super.objects.get(id_nurse=id_nurse)
    user = User.objects.get(username=super.username)
    # pprint(super)
    super.delete()
    user.delete()
    supeer = Super.objects.all()
    messages.success(request,"Data Berhasil dihapus !!") 
    return render(request, 'pages/stisla/master/data-akun.html',{'supeer':supeer})


def insertdata(request):
    global id,rs,usr,em,pwd,tgl_lahir,jk,telp,alamat
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="",database='test')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="id_nurse":
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
        # pprint(age_year)
        c="insert into users Values('{}','{}','{}','{}')".format(usr,em,pwd,"super")
        cursor.execute(c)
        m.commit()
        d="insert into super Values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(id,rs,id_rs,usr,nama,now,tgl_lahir,age_year,jk,alamat,telp)
        cursor.execute(d)
        m.commit()
        supeer= Super.objects.all()
        messages.success(request,"Data berhasil ditambah !!")
        return render(request, 'pages/stisla/master/data-akun.html',{'supeer':supeer})
    return render(request, 'pages/stisla/master/tambah-data.html')
