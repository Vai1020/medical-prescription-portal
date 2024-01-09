from pickle import TRUE
from pyexpat import model
from tkinter import N
from turtle import mode
from django.db import models
from datetime import datetime
# Create your models here.



class regis(models.Model):
    name=models.CharField(max_length=30,default='DEFAULT VALUE',null=True,
   blank=True)
    last_name=models.CharField(max_length=30,default='DEFAULT VALUE',null=True,
   blank=True)
    phone=models.IntegerField(default=00000,null=True,blank=True)
    email=models.EmailField(default='DEFAULT VALUE',null=True,blank=True)
    image=models.ImageField(upload_to='image',default='DEFAULT VALUE')
    regis_number=models.IntegerField(default=00000,null=True,blank=True)
    password=models.CharField(max_length=10,default='DEFAULT VALUE',null=True,blank=True)
   
    def __str__(self):
        return self.name

    @staticmethod
    def get_doctor_by_email(email):
        try:
            return regis.objects.get(email=email)
        except:
            return False
    
 

class prescribe(models.Model):
    gender = (
        ('male', 'male'),
        ('female', 'female'),
        ('other', 'other'),
    )
    name=models.CharField(max_length=30,null=True,blank=True)
    email=models.EmailField(default=' ',null=True,blank=True)
    date=models.DateField(blank=True,null=True)
    age=models.IntegerField(default=00000)
    gender=models.CharField(max_length=8,choices=gender,null=True,blank=True)
    allergy=models.CharField(max_length=20,null=True,blank=True)
    medic=models.CharField(max_length=50,null=True,blank=True)
    time=models.CharField(max_length=50,null=True,blank=True)
    desc=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

    @staticmethod
    def get_all_records():
      return prescribe.objects.all()