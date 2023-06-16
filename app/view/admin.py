from django.shortcuts import render,redirect
from django.utils import timezone
from app.models import Super,User,Admin,Pasien
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

def pasien(request):
    pasiens = Pasien.objects.all()
    return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})

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
        
        c="insert into users Values('{}','{}','{}','{}')".format(usr,em,pwd,"pasien")
        cursor.execute(c)
        m.commit()
        d="insert into pasien Values('{}','{}','{}','{}','{}','{}')".format(id,rs,id_rs,usr,nama,now)
        cursor.execute(d)
        m.commit()
        pasiens= Pasien.objects.all()
        return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})
    return render(request, 'pages/stisla/super/tambah-pasien.html')

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
        
        c="update pasien set id_pasien='{}',rs='{}',id_rs='{}',username='{}',nama_lengkap='{}' where username ='{}' ".format(id,rs,id_rs,usr,nama,username_lama)
        cursor.execute(c)
        m.commit()
        d="update users set username='{}',email='{}',password='{}' where username ='{}' ".format(usr,em,pwd,username_lama)
        cursor.execute(d)
        m.commit()
        pasiens = Pasien.objects.all()
        return render(request, 'pages/stisla/super/data-pasien.html',{'pasiens':pasiens})
    return render(request, 'pages/stisla/super/edit-pasien.html',{'pasien':pasien,'user':user})

def hapuspasien(request, id_pasien): 
    pasien= Pasien.objects.get(id_pasien=id_pasien)
    user = User.objects.get(username=pasien.username)
    # pprint(admin)
    pasien.delete()
    user.delete() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))