from django.shortcuts import render
import mysql.connector as sql

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
        
    return render(request, 'pages/stisla/auth/auth-login-2.html')




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

