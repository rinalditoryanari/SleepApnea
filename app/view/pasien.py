from django.shortcuts import render,redirect
from django.utils import timezone
from app.models import Super,User,Admin,Pasien,Rekaman
from pprint import pprint
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import mysql.connector as sql
from urllib.parse import unquote
from datetime import date,datetime, timedelta
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
import os
import calendar

def editpasien(request):
    # email = unquote(username)
    global id,rs,usr,em,pwd,usr_lama,name
    if request.method=="POST":
        # pprint(admin)
        # pprint(user)global id,rs,usr,em,pwd
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
            if key=="nama_lengkap":
                name=value
            if key=="username":
                usr=value
            if key=="username_lama":
                usr_lama=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
            if key=="no_telp":
                telp=value
            if key=="alamat":
                alamat=value    
        
        # username_rs = request.POST.get("username_rs")

        c="update pasien set id_pasien='{}',rs='{}',id_rs='{}',username='{}',nama_lengkap='{}',alamat='{}',no_telp='{}' where username ='{}' ".format(id,rs,id_rs,usr,nama,alamat,telp,usr_lama)
        cursor.execute(c)
        m.commit()
        d="update users set username='{}',email='{}',password='{}' where username ='{}' ".format(usr,em,pwd,usr_lama)
        cursor.execute(d)
        m.commit()
        rekamans = Rekaman.objects.filter(nama_lengkap=name)
        rekamans = list(rekamans)
        for rekaman in rekamans:
            rekaman = Rekaman.objects.filter(nama_lengkap=name)
            rekaman.update(nama_lengkap=nama)
        messages.success(request,"Data Berhasil diedit !!")
        return render(request, 'pages/stisla/dashboard/pasien.html')
    return render(request, 'pages/stisla/pasien/edit-pasien.html')

def riwayatlaporan(request):
    # rekamans= Rekaman.objects.all()
    return render(request, 'pages/stisla/pasien/riwayat-laporan.html')

def generate_pdf(request,waktu_rekaman):
    # Retrieve the HTML content to convert to PDF
    path_wkhtmltopdf = '/usr/local/bin/wkhtmltopdf'  # This may vary depending on your system
    # config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
    
    # Remove 'T' separator and replace it with a space
    waktu_rekaman = waktu_rekaman.replace('T', ' ')

    # Convert the datetime string to a datetime object
    waktu_rekaman = datetime.strptime(waktu_rekaman, '%Y-%m-%d %H:%M:%S')

    # Retrieve data from the database based on the datetime parameter
    rekamans = Rekaman.objects.get(waktu_rekaman=waktu_rekaman)
    pasiens = Pasien.objects.get(id_pasien=rekamans.id_pasien)
    days = calendar.day_name[waktu_rekaman.weekday()]
    now = timezone.now()

    html = render_to_string('pages/stisla/pasien/cetak-rekaman.html',{'rekamans':rekamans,'pasiens':pasiens,'days':days,'now':now})
    option ={
        'footer-left' :'Dicetak Pada ' + now.strftime('%d/%m/%Y %H:%M:%S')
    }
    pdf = pdfkit.from_string(html, False,configuration=config,options=option)

    # Create a HTTP response with PDF content
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="Hasil_Deteksi.pdf"'
    response.write(pdf)
    # return render(request, 'pages/stisla/admin/cetak-rekaman.html',{'rekamans':rekamans,'pasiens':pasiens,'days':days,'now':now})

    return response

# def hapusdeteksi(request, waktu_dibuat): 
    rekaman = Rekaman.objects.get(waktu_dibuat=waktu_dibuat)
    # pprint(admin)
    rekaman.delete()
    pasiens = Pasien.objects.all()
    messages.success(request,"Data Berhasil dihapus !!") 
    return render(request, 'pages/stisla/admin/data-pasien.html',{'pasiens':pasiens})
