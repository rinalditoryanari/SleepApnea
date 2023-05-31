from django.db import models
class Super(models.Model):
    id_nurse= models.CharField(primary_key=True,max_length=200,blank=True)
    rs=models.EmailField(max_length=500,blank=True)
    id_rs=models.CharField(max_length=200,blank=True)
    username=models.CharField(max_length=200,blank=True)
    nama_lengkap=models.CharField(max_length=200,blank=True)
    waktu_dibuat=models.CharField(max_length=200,blank=True)
    
    class Meta:  
        db_table = "super"
    # location=models.CharField(max_length=200,blank=True,null=True)
# Create your models here.

class User(models.Model):
    username= models.CharField(primary_key=True,max_length=200,blank=True)
    email=models.EmailField(max_length=500,blank=True)
    password=models.CharField(max_length=200,blank=True)
    role=models.CharField(max_length=200,blank=True)

    class Meta:  
        db_table = "users"

class Admin(models.Model):
    id_admin= models.CharField(primary_key=True,max_length=200,blank=True)
    rs=models.EmailField(max_length=500,blank=True)
    id_rs=models.CharField(max_length=200,blank=True)
    username=models.CharField(max_length=200,blank=True)
    nama_lengkap=models.CharField(max_length=200,blank=True)
    waktu_dibuat=models.CharField(max_length=200,blank=True)
    
    class Meta:  
        db_table = "admin"


